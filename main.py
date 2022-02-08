# -*- coding: utf-8 -*-
#/usr/bin/env python3

import json
import os
import time
import requests

requests.packages.urllib3.disable_warnings()

config_path = "./config.json"
sign_in_url = 'https://leetcode-cn.com/accounts/login/'

with open(config_path) as f:
    config = json.load(f)
    OUTPUT_DIR = config['outputDir']
    TIME_INTERVAL = 3600 * 24 * config['time']

EXTENSION = {"C++": ".cpp", "Python3": ".py", "Python": ".py", "MySQL": ".sql", "Go": ".go", "Java": ".java",
                "C": ".c", "JavaScript": ".js", "PHP": ".php", "C#": ".cs", "Ruby": ".rb", "Swift": ".swift",
                "Scala": ".sacla", "Kotlin": ".kt", "Rust": ".rs", "MS SQL Server": ".sql", "Oracle": ".sql", 
                "TypeScript": ".ts", "Racket": ".rkt", "Erlang": ".erl", "Elixir": ".ex", "Bash": ".sh"}

COMMENT = {"C++": "//", "Python3": "#", "Python": "#", "MySQL": "--", "Go": "//", "Java": "//",
                "C": "//", "JavaScript": "//", "PHP": "//", "C#": "//", "Ruby": "#", "Swift": "//",
                "Scala": "//", "Kotlin": "//", "Rust": "//", "MS SQL Server": "--", "Oracle": "--", 
                "TypeScript": "//", "Racket": ";;", "Erlang": "%%", "Elixir": "#", "Bash": "#"}

HEADERS = {
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }   

def get_problems():
    while True:
        try:
            problem_url = "https://leetcode-cn.com/api/problems/all/"
            resp = requests.Session().get(problem_url, headers = HEADERS, timeout = 10).content.decode('utf-8')
            question_list = json.loads(resp)
            difficulty = {1 : 'Easy', 2 : 'Medium', 3 : 'Hard'}
            problem_id_dict = dict()
            level_dict = dict()
            for question in question_list['stat_status_pairs']:
                frontend_question_id = question['stat']['frontend_question_id']
                question_title_slug = question['stat']['question__title_slug']
                level = difficulty.get(question['difficulty']['level'],'Unknown')
                problem_id_dict[question_title_slug] = frontend_question_id
                level_dict[question_title_slug] = level
            print("Get problem list Succeeded!")
            return (problem_id_dict,level_dict)
        except Exception as e:
            print(e, "Get problem list failed! Will try again.")
            time.sleep(10)

def login():
    client = requests.session()
    client.encoding = "utf-8"
    while True:
        try:
            with open(config_path) as f:
                config = json.load(f) 
                login_data = {
                    'login': config['username'],
                    'password': config['password']
                }
            client.get(sign_in_url, verify=False)
            result = client.post(sign_in_url, data = login_data, headers = dict(Referer = sign_in_url))
            if result.ok:
                print("Login Succeeded!")
                break
        except Exception as e:
            print(e, "Login failed! Will try again.")
            time.sleep(10)
    return client

def handle(client, problem_id_dict, level_dict):
    page = 0
    downloaded = set()
    download_count = 0
    error_submission_list = []
    break_2 = False
    current_time = time.time()
    while True:
        submissions_url = "https://leetcode-cn.com/api/submissions/?offset=" + str(page) + "&limit=20&lastkey="
        html = client.get(submissions_url, verify=False).text
        html = json.loads(html)
        for submission in html["submissions_dump"]:
            problem_title = submission['title'].replace(" ","")
            submission_language = submission['lang']
            if submission['status_display'] != "Accepted":
                continue
            if current_time - submission['timestamp'] > TIME_INTERVAL:
                print("Reach time interval.")
                break_2 = True
                break
            try:
                code, problem_id, problem_url = downloadCode(submission, client, problem_id_dict, level_dict)
                if problem_id == "":
                    print("Cannot find problem id for:" + problem_title + ". Problem Url:" + problem_url)
                filename, full_path = generatePath(problem_id, problem_title, submission_language)
                if filename not in downloaded:
                    with open(full_path, "w") as f:
                        f.write(code)
                        print("Wrote file to:", full_path)
                    download_count += 1
                    downloaded.add(filename)  
            except Exception as e:
                print(e, "ERROR. Will try again.")
                error_submission_list.append(submission)
        print ("Download count:", str(download_count))
        print ("End of page:", str(page))
        if break_2 or (html['has_next'] == False):
            print("End.")
            break
        page += 20
        time.sleep(20)
    retry_count = 0
    if len(error_submission_list) > 0:
        print("Now Retrying for", str(len(error_submission_list)), "submissions.")
        for submission in error_submission_list:
            time.sleep(1)
            problem_title = submission['title'].replace(" ","")
            submission_language = submission['lang']
            code, problem_id, problem_url = downloadCode(submission, client, problem_id_dict, level_dict)
            if problem_id == "":
                print("Cannot find problem id for:" + problem_title + ". Problem Url:" + problem_url)
            filename, full_path = generatePath(problem_id, problem_title, submission_language)
            if filename not in downloaded:
                with open(full_path, "w") as f:
                    f.write(code)
                    print("Wrote file to:", full_path)
                download_count += 1
                downloaded.add(filename)
                retry_count += 1
                if retry_count % 5 == 0:
                    time.sleep(10)
    print("Total Download count:", str(download_count+retry_count))
    print("Success!")
    return 0

def downloadCode(submission, client, problem_id_dict, level_dict):
    param = {'operationName': "mySubmissionDetail", "variables": {"id": submission["id"]},
                'query': "query mySubmissionDetail($id: ID\u0021) {  submissionDetail(submissionId: $id) {    id    code    runtime    memory    statusDisplay    timestamp    lang    passedTestCaseCnt    totalTestCaseCnt    sourceUrl    question {      titleSlug      title      translatedTitle      questionId      __typename    }    ... on GeneralSubmissionNode {      outputDetail {        codeOutput        expectedOutput        input        compileError        runtimeError        lastTestcase        __typename      }      __typename    }    __typename  }}"
                    }
    param_json = json.dumps(param).encode("utf-8")
    response = client.post("https://leetcode-cn.com/graphql/", data = param_json, headers = HEADERS).json()
    submission_details = response["data"]["submissionDetail"]
    title_slug = submission_details["question"]['titleSlug']
    english_name = submission_details["question"]['title']
    chinese_name = submission_details["question"]['translatedTitle']
    original_code = submission_details["code"]
    #submit_time = submission_details["question"]['timestamp']
    problem_url = "https://leetcode-cn.com" + submission_details["sourceUrl"]
    problem_id = problem_id_dict.get(title_slug, "Unknown")
    problem_level = level_dict.get(title_slug, "Unknown")
    submit_lang = submission['lang']
    lang_comment = COMMENT.get(submit_lang, "//")
    prefix = lang_comment + " Problem Id:  " + problem_id + "\n"
    prefix += lang_comment + " Problem Name:  " + english_name + ", " + chinese_name + "\n"
    prefix += lang_comment + " Problem Url:  " + problem_url + "\n"
    prefix += lang_comment + " Problem Level:  " + problem_level + "\n"
    prefix += lang_comment + " Language:  " + submit_lang + "\n \n"
    code = prefix + original_code
    return code, problem_id_dict.get(title_slug, ""), problem_url

def generatePath(problem_id, problem_title, submission_language):
    ext = EXTENSION.get(submission_language,submission_language)
    if problem_id == "":
        filename = problem_title + ext
    elif problem_id[0].isdigit():
        filename = '{:0=4}'.format(int(problem_id)) + "-" + problem_title + ext
    else:
        filename = problem_id + "-" + problem_title + ext
    filename = filename.replace(" ", "")
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
    full_path = os.path.join(OUTPUT_DIR, filename)
    return filename, full_path

def main():
    problem_id_dict,level_dict = get_problems()
    client = login()
    handle(client, problem_id_dict, level_dict)

if __name__ == '__main__':
    main()