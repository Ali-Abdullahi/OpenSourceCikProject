import requests
import json
class SecEdgar:
    def __init__(self,fileur1):
        self.fileur1=fileur1
        self.namedict={}
        self.tickerdict={}


        headers={'user-agent': 'MLT CP Ali.Abdullahi1228@gmail.com'}
        r=requests.get(self.fileur1,headers=headers)
        self.r_json=json.loads(r.text)

        self.filejson=r.json

       
    
            

            

        self.cik_json_to_dict()

    def cik_json_to_dict(self):
        self.name_dict = {}
        self.ticker_dict={}

        for row in self.r_json['data']:
            company_ticker= row[2]
            company_id=row[0]
            self.ticker_dict[company_ticker]=company_id
        

        for row in self.r_json['data']:
            company_name= row[1]
            company_id=row[0]
            self.name_dict[company_name]=company_id
        

    def ticker_to_Cik(self,input):
        output=[]
        output.append(input)
        output.append(self.ticker_dict[input])
        id=self.ticker_dict[input]
        name= list(self.name_dict.keys())[list(self.name_dict.values()).index(id)]
        output.append(name)
        return output




    def name_to_Cik(self,input):
        output=[]
        output.append(input)
        output.append(self.name_dict[input])
        id=self.name_dict[input]
        name= list(self.ticker_dict.keys())[list(self.ticker_dict.values()).index(id)]
        output.append(name)
        return output
        

        

se=SecEdgar('https://www.sec.gov/files/company_tickers_exchange.json')


if __name__=="__main__":
    # result=se.ticker_to_Cik("AAPL")
    result_2=se.name_to_Cik("Apple Inc.")
    print(result_2)

