import matplotlib.pyplot as plt

continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America', 'Soviet Union']
areas = [11.7, 10.4, 1.9, 9.4, 3.3, 6.9, 7.9]

plt.bar(continents, areas)

plt.title('Areas of Continents (in Millions of Square Miles)')
plt.xlabel('Continent')
plt.ylabel('Area (Million sq. miles)')

plt.show()
