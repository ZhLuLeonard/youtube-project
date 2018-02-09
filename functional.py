"""
First attempt to automate search for qaulity firles on youtube

Principles:
1. Priorize labelled and processed videos
2. Focus on human speech
3. Using youtube subtitles
4. Compliment existing voice data with search results
5. Present in the most convenient way
6. First realization, then improve

Modules:
1. query: finding all qualified videos
2. local setup
3. video procesing: subtitle management/post-processing
4. Labelling and storage

Timeline:
January:
1,3
Feb:
2,4
March:
Machine Learning Model
------------------------------------------------------------------------

"""

#Todo:
#1.find according youtube video links from files
#2.download the files (audio only)
#3.use another module to analyze the subtitles
#4.Perform below operations on the files:
    #Delete
    #Cut
    #Store

"""
Update: 
01/17: tried to learn tensorflow, failed to install, decide to use FloyHub
Next: Learn tensorflow: goal: to get tensorflow model running on videoes by 2/1
"""

import subprocess
import os
import json

#Set up environment(youtube downloads file, data query file)
def main():
    DEFAULT = ".\Video"
    Ontology = ".\ontology"
    if not os.path.exists(DEFAULT):
        os.makedirs(DEFAULT)
    os.chdir(DEFAULT)
    if not os.path.exists(Ontology):
        subprocess.run('git clone https://github.com/audioset/ontology.git')
    os.chdir(Ontology)
    with open("ontology.json",'r') as f:
        datastore = json.load(f)
    print(query(datastore,"shout"))

#query the id of labels related to the search
#Returns a list of the ids(strings)
def query(data, ins):
    out=[]
    confirm = []
    inp = ins.lower()
    if inp == "":
        return confirm
    else:
        for item in data:
            if item["name"].lower()==inp:
                out.append(item)
        while len(out)!=0:
            finished = out.pop()
            confirm.append(finished['id'])
            for child in finished['child_ids']:
                if child not in confirm:
                    for i in data:
                        if i['id']==child:
                            out.append(i)
    return confirm

#subprocess.run('youtube-dl --write-auto-sub https://www.youtube.com/watch?v=TmjjHbUb4jc')

if __name__=="__main__":
    main()