import pandas as pd
data={"year":[2010,2010,2012,2010,2012],"month":["jan","mar","jan","dec","dec"],"passengers":[25,50,35,55,65]}
df=pd.DataFrame(data)
print(df[['year','passengers']][df['year']==2010])
