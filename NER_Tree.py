#coding:utf-8
# 顏面部撕裂傷，騎車汽車發生車禍致鼻樑撕裂傷，雙鼻鼻血，右側肢體擦傷，身上有汽油味
import time
class treeNode:
    def __init__(self, nameValue):
        self.name = nameValue
        self.children = {}
        self.isEnd = 0

    def disp(self, ind=1):
        with open("display.txt",encoding="utf-8",mode="a") as f:
            f.write(' '*(ind) + str(self.name) + str(self.isEnd) + ' ' + "\n")
         
        print(' '*(ind), self.name,self.isEnd, ' ')
        for child in self.children.values():
            child.disp(ind+1)
        
def updateTokenTree(items, inTree):
    # print(items)

    if items[0] not in inTree.children:
        inTree.children[items[0]] = treeNode(items[0])
        if len(items) == 1 :
            # print("end : ",inTree.children[items[0]].name)
            inTree.children[items[0]].isEnd = 1
            # print("end : ",inTree.children[items[0]].isEnd)
            
    if len(items) == 1 and items[0] in inTree.children:
        inTree.children[items[0]].isEnd = 1
        
    if len(items) > 1:
        updateTokenTree(items[1::], inTree.children[items[0]])
    
    

def createTokenTree(dataset):
    retTree = treeNode("Null")
    for trans in dataset:
        updateTokenTree(trans, retTree)

    return retTree

def LoadData(DictFile):

    with open(DictFile,mode="r",encoding="utf-8") as file:
        test_data = []
        for line in file:
            test_data.append(line.strip().encode('utf-8').decode('utf-8-sig'))

    data = list(map(list,test_data))
    return data

def mineTree(TokenTree, sentence, a, EndFlag = 0):
    # a = 0
    EndFlag = TokenTree.isEnd
    # print(f"a is {a}", TokenTree.name, EndFlag, sentence[0:a])
    
    
    if a <= (len(sentence) - 1):
        if sentence[a] in TokenTree.children:
            a = a + 1
            a, EndFlag = mineTree(TokenTree.children[sentence[a-1]], sentence, a, EndFlag)
    
    
    
    return a, EndFlag


def tokenize(TokenTree,sentence):
    toke=[]
    sentencelen =  len(sentence)
    StartIndex = 0
    Endflag = 0
    while sentencelen != 0:
        a = 0
        a, Endflag = mineTree(TokenTree, sentence, a)
        # print(f"a is {a}, ", sentence[0:a], Endflag)
        # print("======================")
        if a == 0 :
            sentence = sentence[1:len(sentence)]
            sentencelen = len(sentence)
            StartIndex += 1
        elif a == 1 :
            
            
            if Endflag:
                toke.append([sentence[0:a],StartIndex,StartIndex+a-1])
                StartIndex += a
                sentence = sentence[a:len(sentence)]
                sentencelen = len(sentence)
            else :
                StartIndex += a
                sentence = sentence[a:len(sentence)]
                sentencelen = len(sentence)
                
        
        else :
            # print(sentence[0:a], "" , Endflag)
            if Endflag:
                toke.append([sentence[0:a],StartIndex,StartIndex+a-1])
                StartIndex += a
                sentence = sentence[a:len(sentence)]
                sentencelen = len(sentence)
            else :
                StartIndex += a
                sentence = sentence[a:len(sentence)]
                sentencelen = len(sentence)
        
    return toke

def Combine(AfterTokenizeList):
    flag = 0
    output = []
    temp = []
    for i in AfterTokenizeList:
        if len(i) != 1:
            if flag == 0:
                output.append(i[::])
            else :
                output.append("".join(temp))
                output.append(i[::])
                temp = []
                flag = 0
                
                
        else :
            if flag == 0:
                temp.append(i)
                flag = 1
            else :
                temp.append(i)
    print(output)
    return 0


#開始計時
if __name__ == '__main__':
    
    Body = "Body.txt"
    Symptom = "symptom.txt"
    
    now = lambda : time.time()
    
    start = now()
    # Loading Dictionary
    Body_Data = LoadData(Body)
    Symptom_Data = LoadData(Symptom)
    
    Body_tree = createTokenTree(Body_Data)
    Symptom_tree = createTokenTree(Symptom_Data)


    
    print(f"Build Token Tree Time : {now()-start}")
    while True:
        print("=============================================================================================")
        sentence = input('請輸入文字 (輸入q以結束程式): ')
        if sentence !='q':
            
            #開始計時
            start = now()
            
            print("Body : ")
            Body_toke = tokenize(Body_tree, sentence)
            print(Body_toke)
            # Combine(toke)
            
            print()
            print("Symptom : ")
            Symptom_toke = tokenize(Symptom_tree, sentence)
            print(Symptom_toke)
            
            print(f"執行時間: {now() - start} 秒")

            print("Sentence length : ",len(sentence))

        else: break