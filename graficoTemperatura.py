from pylab import plot, show, legend, title, xlabel, ylabel
import matplotlib.pyplot as plt


meses = ['Jan', 'Fev', 'Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
Tmax = [38,39,32,29,26,22,19,15,20,22,25,27]
Tmin = [23,23,22,21,19,16,12,10,16,21,22,22]
plt.plot(meses,Tmax,meses,Tmin)

title('Temperaturas Maximas e Minimas do Ano')
xlabel('Mes')
ylabel('Temp/ºC')
legend(['Tmax','Tmin'])

plt.savefig('ImgTemp.png',format='png', transparent = True)

plt.show()