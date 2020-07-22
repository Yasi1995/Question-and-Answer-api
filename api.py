#! /usr/bin/env python
# coding: utf-8
from flask import Flask, jsonify, request
import subprocess
import QuestionNet as qn



app = Flask(__name__)

sampleJson = {"question":{"0":"What is bond angle of NaOH?","1":"What is bond angle of KOH?"},"answer":{"0":{"0":"120","1":"100","2":"200","3":"300"},"1":{"0":"120","1":"100","2":"200","3":"300"}}}

level2 = {"question":{"0":"What is bond angle of yyy?","1":"What is bond angle of KOH?"},"answer":{"0":{"0":"yyy","1":"100","2":"200","3":"300"},"1":{"0":"120","1":"100","2":"200","3":"300"}}}

level3 = {"question":{"0":"What is bond angle of zzz?","1":"What is bond angle of KOH?"},"answer":{"0":{"0":"zzz","1":"100","2":"200","3":"300"},"1":{"0":"120","1":"100","2":"200","3":"300"}}}
# anss={"0":"The people"}
# print(anss[0])


@app.route('/incomes')
def get_incomes():
	questionNet = qn.QuestionNet()
	return questionNet.makeJson()

@app.route('/test')
def get_test():
	
	return jsonify(sampleJson)

@app.route('/level2')
def get_level2():
	
	return jsonify(level2)

@app.route('/level3')
def get_level3():
	
	return jsonify(level3)




if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5010,threaded=True)
