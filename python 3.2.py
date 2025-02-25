import pandas as pd
data={"House":["Green","Yellow","Pink","Blue"],"First":[5,10,8,10],"Second":[7,5,13,5],"Third":[6,4,15,3]}
df=pd.DataFrame(data)
df['Points']=df['First']+df['Second']+df['Third']
df=df.sort_values(by=['Points'],ascending=False)
print(df)
