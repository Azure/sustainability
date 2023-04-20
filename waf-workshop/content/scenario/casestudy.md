---
title: "Case study"
date: 2022-09-22T12:45:35+01:00
draft: false
weight: 1
---

##### Directions
- Read the customer case study and current customer environment.
- Identify the key points of the customer case study and current environment. Use the table after the case study to make any relevant notes.
- Build one or two slides in preparation for the final presentation (Step 4) including the following:
    - Customer case study key points. 
    - Main characteristics of the current customer environment.

{{% notice style="note" %}}
The focus of this step is becoming familiar with customer case study, while Step 2 is dedicated to solution architecture.
{{% /notice %}}


##### Case study
Contoso is a highly respected business leadership academy based in London, United Kingdom with more than 150,000 members in the region and another 2,500,000 worldwide. They deliver in-person training, online seminars and Massive Open Online Courses (MOOCs).

Among their various cohorts there is alignment between their curriculum and the [UN Sustainable Development Goals (SDGs)](https://sdgs.un.org/goals) as well as with the [UK’s Net Zero Strategy](https://www.gov.uk/government/publications/net-zero-strategy) which sets our policies and proposals for decarbonizing all sectors of the UK economy to meet their net zero target by 2050.

Furthermore, Contoso’s corporate and social responsibility (CSR) “3D strategy” defines the following key goals:
- Deeply care about their staff, their academia and their partners to build and nurture fruitful collaboration while delivering the best results.
- Develop best-of-breed leaders to tackle key challenges of today while mitigating the ones of tomorrow.
- Deploy the most sustainable, securely trusted and innovative solutions to drive benefits for their academia and also across society.

Currently, the academy runs IT workloads in an on-premises datacenter where it has invested in and completed an IT modernization project approximately 2 years ago. As a result, their board has been very reluctant to adopt new cloud technologies not only due to budget constraints but also because of the reduced amount of staff dedicated to manage their environments. 

That said, the academy was unfortunately targeted by a cybersecurity attack which compromised over 275,000 user accounts among their academia and staff compromising the access to their main MOOC portal for over two weeks. Such infrastructure was predominantly reliant on virtual machines running a frontend web-farm connected to a SQL highly-available backend system. The backend not only hosts a whole raft of material (including 70TB of video content) accounting for approximately 90% of all of their storage but is also very costly and reaching end-of-life in 14 months. The incident took a lot longer to resolve due to the lack of advanced security technology and rudimentary incident response mechanisms.

When attending [COP27](https://cop27.eg/), Contoso’s CTO met with a Microsoft representative to discuss the potential benefits of adopting Microsoft Azure in alignment with their 3D strategy to help with reducing their carbon footprint and drive adoption of advanced cloud-native services for their MOOC platform. This would allow a pivot towards other innovative use cases leveraging their pool of data through the adoption of services such as Azure Cognitive Search and Azure Video Analyzer for Media.

As a result, Contoso now aims to retire as much of their datacenter footprint to allow them to:
1. Increase the security posture across their infrastructure.
2. Reduce the administrative burden on their teams by leveraging platform-as-a-service or other cloud-native services where possible.
3. Reduce and optimize their carbon footprint as a result of adopting Microsoft Azure.

For a start and based upon the above, their plan is to migrate their MOOC platform into Azure – that is the scope of this exercise.