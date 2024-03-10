# Internship_2020 - University of Twente
Scheduling/Queuing tool for CTT Hengelo's Rotterdam terminal

ADR is the European Agreement which concerns the International Carriage of Dangerous Goods by Road. ADR includes a special procedure in road traffic in regards to packaging, 
cargo insurance and labeling of dangerous goods and ADR goods can be divided into nine sub-categories. Such containers should not be needlessly moved around unless it is absolutely
required. The priority list for ADR containers contains a list of containers that are recommended to picked up or processes first i.e., should be prioritized. The underlying method
behind this fairly simple. The Rotterdam terminal is divided into regions, subregions and in certain regions and subregions only ADR containers are stored. This information can 
found be founded from ‘CURRENTPOSITION’ column of our final data (This can be seen in the data snapshot). The system checks for this information and separates the ADR and non-ADR
containers and then based on the position where the container is stacked that container is then included in the priority list. An example for this would be whether or not a 
container is on the top or just below another container, then those containers can be included in the priority list. These two lists can be exported from the system in multiple
formats and can be presented in a dashboard. In our case we exported the data in the form of .csv files to use in our Power BI dashboard.  

The priority list does not indicate that only containers present in that list can be processed, it means that it is better for CTT if these containers are moved first, as this should result in a decrease of unnecessary moves. CTT can also use this list and specify a timeslot for truck-drivers for picking up those containers
