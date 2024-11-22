from os import pathsep
class TextAnalytics:
    def __init__(self,IFP=str,OFP=str,IWFP="",CW=1):
        self.Checked = False
        self.Data = {"IFP" : IFP ,"OFP" : OFP ,"IWFP" : IWFP};
        self.CW = CW
        if self.Checked is False:
            self.Check()
    def Check(self):
        Errorpath = ""
        try:
            open(self.Data["IFP"],"r")
            open(self.Data["OFP"],"r")
            if self.Data["IWFP"] == "":
                pass
            else:
                open(self.Data["IWFP"],"r")
        except FileNotFoundError as i:
            for j in self.Data.items():
                if j[1] == i.filename:
                    Errorpath = j[0]
                    break
            self.Data[Errorpath] = input(f"the {Errorpath} is incorrect. please rewrite the path: ")
            self.Check()