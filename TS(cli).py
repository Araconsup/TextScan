from os import pathsep
class TextAnalytics:
    def __init__(self,IFP=str,OFP=str,IWFP="",CW=1):
        self.Checked = False
        self.Data = {"IFP" : IFP ,"OFP" : OFP ,"IWFP" : IWFP};
        self.CW = CW
        self.IgnoreFileEmpty = False
        if self.Checked is False:
            self.Check()
    def Check(self):
        Errorpath = ""
        try:
            open(self.Data["IFP"],"r")
            open(self.Data["OFP"],"r")
            if self.Data["IWFP"] == "":
                self.IgnoreFileEmpty = True
            else:
                open(self.Data["IWFP"],"r")
        except FileNotFoundError as i:
            for j in self.Data.items():
                if j[1] == i.filename:
                    Errorpath = j[0]
                    break
            self.Data[Errorpath] = input(f"the {Errorpath} is incorrect. please rewrite the path: ")
            self.Check()
    def IgnoreWord(self):
        if self.IgnoreFileEmpty is True:
            with open(self.Data["IWFP"], "r") as IW:
                self.IgnoreWords = IW.read().split("\n")
    def ConsecutiveWords(self):
        for i in range(0,len(self.InputText),self.CW):
            j = i+(i+self.CW)
            tmp = self.InputText.split(" ")
            tmp[i].join(tmp[j])
            continue
    def Analyzer(self):
        with open(self.Data["IFP"],"r") as IF:
            self.InputText = IF
            self.IgnoreWord()
            self.ConsecutiveWords()

            


        