.PHONY: data

scatter:
	python -B src/test_scatter.py
hiv:
	python -B src/hivdata.py

data:
	mkdir -p data
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/county.csv?token=GHSAT0AAAAAAB5KSRG3UMFQDFGWDGNDRUPCZAXKC7Q
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/county45_54.csv?token=GHSAT0AAAAAAB5KSRG27EZ6JEO2F3H54WU6ZAXKDNQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/county55%2B.csv?token=GHSAT0AAAAAAB5KSRG2IR5EA6AWIGVNHE3MZAXKD5A
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/scat3.csv?token=GHSAT0AAAAAAB5KSRG3Z45QMBWV6WEM5ZFMZAXKENQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/AIDSVu_County_SDOH_2020.csv?token=GHSAT0AAAAAAB5KSRG3PY4XJTCOFIJWOXUKZBAQ5NQ
	cd data; curl -LO https://raw.githubusercontent.com/ds5110/projects-spring-2023-ahaskell83/main/data/scat4.csv?token=GHSAT0AAAAAAB5KSRG2AQPHCTC7Z4THKARKZBAQ57A

clean:
	rm data/couty.csv
	rm data/county45_55.csv
	rm data/county55+.csv
	rm data/scat3.csv
	rm data/AIDSVu_County_SDOH_2020
	rm data/scat4
