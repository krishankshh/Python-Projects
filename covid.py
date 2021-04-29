import covid
import matplotlib.pyplot as plt
covid = covid.Covid()
name = input('Enter the name of country')
virusdata = cov.get_status_by_country_name(name)
active = virusdata['Active']
recover = virusdata['Recovered']
deaths = virusdata['Deaths']
plt.pie([Active,Recover,Deaths],labels = ['Active','Recovered','Deaths'], colors = ['b','g','r'],explode = (0,0,0,2),startangle = 180,autopct = '%1.1f%%',shadow = True)
plt.title(name)
plt.legend()
plt.show()
