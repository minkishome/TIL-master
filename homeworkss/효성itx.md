조직 속에 있지만 새로운 사업 계속해서 추구

발전 기대가 크다

[다른](#C:\Users\minki\Desktop\빅데이터자료.md) 대기업과 다르게 IT 산업 특성에 맞는 형태 (스마트컨택센터 클라우드 4개월만에 )

서류 코테 없이 바로 면접



8월 중으로 바로 면접

9월 초반 입사

시장에 대한 흐름

클라우드 컨택트에 대한 기본적인 개념 + 내가 했던거랑 연계

시장과 산업에 대한 관심 + 새로운것을 해보겠다는 것들

내가 어려움을 이겨내는 방법 어떻게 

신뢰 비젼 하고싶음을 어필







### 클라우드 컨텍센터 고려될 기술적 사항

1. **Cloud 컨택센터는 중앙 집중식이므로 대량의 데이터를 처리할 수 있는 능력이 있어야 한다.**
2. **중앙에 집중된 여러 자원들을 필요한 만큼씩 나누어서 독립적으로 활용할 수 있도록 하기 위한 기능으로서는 Multi Tenancy 가 있다.**
3. **마지막으로 필요한 것은 네트워크를 통한 보안이다.**
   -  데스크톱 가상화(VDI)
     1. 비용
     2. PC의 관리적 요소
     3. 보안





```
기존의 대규모 콜센터를 클라우드 기반으로 이전? --> 단순히 음성만을 활용하지 않고 다양한 형태의 데이터를 입력 받을 것이기에 그와 관련된 처리 능력이 필수적  // 보이스, 메일, 소셜 미디어 등 다양한 채널로 확대
```

```
다양한 데이터를 받고 이를 분석할 수 있는 능력?
커뮤니케이션 - 팀원들과 함께 대화 그리고 고객들에게 기술을 더 쉽게 표현할 수 있는 능력?

```

```
#클라우드에서 필요한 것 - 보안?

```



![image-20200807170354356](C:\Users\minki\AppData\Roaming\Typora\typora-user-images\image-20200807170354356.png)

- System, Infra 구축, 

# 클라우드 컨택트 센터 시장

23년 까지 연평균 25%성장, 71억달러 -> 266억달러로 성장

IT 기술의 가장 큰 장점인 digital transformation을 가장 잘 보여주는 산업이라 생각

#현재 코로나로 인해 이러한 성장세는 더 크게 나타날 것으로 예상된다

고객들도 전화보다 점점 텍스트를 활용한 서비스를 원하고 있다.

크게 single-tenancy, multi-tenancy로 나뉜다.

대체로 어느정도 규모가 있는 회사들에 필요한 서비스이며 그러한 점에서 성장할 가능성이 더욱 높다. 

```
diff // 해석
Single - customized software platform that connects to the on-premises applications. While this is the more expensive solution, it offers a higher level of security in general, as each customer’s data is kept separate, and downtime for another customer does not affect other customers. 

Multi -  the software gets hosted in the cloud at the UCaaS provider data center, and not locally. In a multi-tenancy setup, all the customers of the UCaaS share a single software platform. This offers multiple advantages, including higher reliability, a lower cost, and the ability to offer more support, including provisioning of software upgrades. The disadvantage of multi-tenancy, compared to the single-tenancy model, is that it offers fewer options for customization.
```

PBX(Private branch exchange)를 대체할 수 있다. /// 

```
PBX
 allow multiple users to share a limited number of outside phone lines via a system that gives each user, including devices such as fax machines, an extension, thereby saving money rather than having an individual dedicated phone line for each. There are additional savings with internal phone calls between users. However, with a PBX, the corporation has to purchase the PBX hardware, with acquisition prices in the thousands, and then be responsible for supporting it in house. 
 
DIFF PBX
In this setup, all the phones connect only through the internet, with no direct wiring between them. The company outsources all the maintenance and software to the Business VoIP provider.  This enables the features of the traditional PBX as older systems, such as having multiple users able to share a limited number of lines and internal calling between extensions.

However, being cloud-based enables additional functionality, including enabling a direct phone number, group intercom paging, voicemail to email, and internet faxing. Equally important, it also enables integration with popular business platforms, including Skype for Business, Zendesk, Salesforce, and Outlook; the last integration allows a user to be able to make a phone call from right within the body of the email. 
```

```
5. Greater Mobility

UCaaS is a strong enabler for the mobile worker, the BYOD explosion, and remote/home office worker. It allows users access to all business communications features from any registered user device, including a smart phone, laptop, desktop and, of course, desk phone. Organizations can enable users’ smart phones to transparently bridge calls from the company’s Wi-Fi networks to cellular networks and back again, keeping “on-the-go” and “location agnostic” users connected. Desktop client software can turn any networked PC into a virtual desktop phone and unified messaging terminal. Users can travel with their extensions, use video conferencing, and access advanced call forwarding and web-browser dialing. IT organizations often struggle with managing application across numerous devices. With UCaaS, users download the device application from the app store and IT can easily manage their access. An additional user benefit is that the experience is the same across all devices.

```



### 효성 클라우드 컨택트 센터

코로나로 인해 많은 성장 -> 현재 다양한 콜센터 회사들을 중심으로 계속해서 성장해 나가는 중



Difference between contact center vs call center

```
VoIP Telephone Services
Email
Text Chat
Fax services
Direct Website Interface
 ///////// contact center provides
```





### 장점

```
1. 파이썬을 통한 데이터 처리 능력???
2. aws 사용, container에 대한 이해
```

```

Top Benefits of a Cloud-Based Contact Center
Most of the contact centers in operation today are running on old technology and call center software that can’t keep up with the way customers and businesses now communicate. A cloud-based contact center is a modern alternative to on-premise contact centers using the latest in communications technology. It offers many benefits to businesses who want to continually meet and exceed their customers’ expectations.
```

```
AWS에서 제공하는 EC2가 대표적인 예이다. 이는 단순히 서버 등의 자원을 제공해 주면서 사용자가 디바이스에 제약없이 데이터에 접근할 수 있도록 해준다. // IaaS
서비스로서의 소프트웨어 (SaaS) 
Iaas Saas 그 사이인듯
개발 자유도도 훨씬 높고 의욕적인 사람도 많아 업무 만족도도 높습니다.
```





도커 이미지 : 읽기 전용으로 개발자가 테스트 등에 사용, 템플릿임 

컨테이너 -> 이미지를 읽고 running 할 수 있다. 그리고 이미지들을 여기서 변환 시킬 수 있다.

![image-20200806151522342](C:\Users\minki\AppData\Roaming\Typora\typora-user-images\image-20200806151522342.png)







### For Cloud

1. Linux - IT runs on the cloud, and the cloud runs on Linux
2. Programming - development, systems support, networking, security, or design 여기서 내가 할 수 있는 건 개발 - 결국 Java를 얼마나 빠르게 배울 수 있는지가 중요
3. Database Management (Database-as-a-Service (DBaaS)) -  NoSQL is becoming popular as an alternative to the limitations of SQL’s rigid schema.

4. Multi-Cloud Deployment 

5. Artificial Intelligence and Machine Learning
6. Automation
7. Serverless Architecture - Cloud services continue to multiply beyond [the SaaS](https://www.cbtnuggets.com/blog/career/career-progression/how-important-is-automation-in-it), IaaS, and PaaS that we learned long ago when first studying cloud computing.
8. Devops - *DevOps is the practice of operations and development engineers participating together in the entire service lifecycle, from design through the development process to production support.*

9. Cloud Security

10. Adaptability

### Cloud Migration Strategies // 다양한 환경에 적용시키는 것

11. change Management
12. Hybrid Cloud
13. Cloud Provider Selection





```
<신기술을 통한 Digital Transformation>
삼성전자 청년 소프트웨어 교육을 통해 신입 개발자로 꿈을 키워 나가며 어떤 개발자가 될 것인가에 대한 많은 생각을 하였습니다. IT 기술을 배우며 저 스스로 가진 개발자의 정의는 "새로운 기술을 통해 기존 산업의 비효율을 효율적으로 바꾸는 것" 입니다. 이러한 생각에 효성 ITX의 그간의 사업과, 입사 후 맡게 될 업무를 생각했을 때 제가 생각하는 개발자 그 이상을 이룰 수 있을 것이라 생각하여 지원하였습니다. 통신기술의 발전은 클라우드라는 기술의 빠른 발전을 만들었고 해당 기술을 활용한 산업은 계속해서 성장할 것이라 생각합니다.
이러한 변화에서 효성 ITX의 클라우드 컨택트 센터와 함께 스스로 성장할 수 있을 것이라 생각합니다. 저는 클라우드 기술을 활용해 변하는 산업을 따라갈 수 있는 능력을, 고개들에겐 더 나은 근무환경과 다양한 채널을 제공해 더 효율적인 환경을 제공할 수 있을 것입니다. 특히 기존의 콜센터들이 전화에 집중하는 것을 넘어 이메일, 메신저 등 더 다양한 채널을 제공하며 더 효율적으로 업무를 진행할 수 있을 것입니다. 
이처럼 현재 효성ITX의 클라우드 서비스는 제가 생각하는 개발자의 역할을 모두 이룰 수 있는 기회를 줄 것입니다. 그 속에서 더 나은 개발자, 더 나은 사원으로 성장해 더 큰 가치를 만들어 내도록 노력하겠습니다. 

```



클라우드 컨택트 센터 - 기존 전화 위주의 고객과의 채널을 더 다양한 방법으로 확장하는 것

결국 효성ITX가 보유하고 있는 기술을 고객들에게 제공 --> 서비스 제공 근데 기존의 Iaas, Saas, Paas처럼 구분되지 않고 이것들이 함께 이뤄지는 것

개발자로 기술에 대한 정확한 이해도 필요함과 동시에 고개들에게 이를 정확하게 이해시키고 설명하는것? 그러한 것들 역시 필요하다고 생각

또한, 파이썬을 공부하고, 과거 대학을 다니며 데이터 분석 프로젝트를 경험하며 데이터와 관련된 업무에 있어 장점이 있다고 생각한다. 제가 찾아본 바로는 클라우드 컨택센터에선 기존과 다르게 더 다양한 채널이 이루어지며 이로인해 수집할 수 있고, 처리해야할 데이터가 상당할 것이기에 제가 가진 그러한 장점을 효과적으로 사용할 수 있다고 생각합니다. 



가장 중요한것? 

아무래도 보안이라고 생각한다. 고객들의 정보들이 유출되면 안되기에 이러한 부분에 있어 더 효과적인 보안이 필요할 것

두번째는 해당 고객에게 어떤 기술이 필요한지 Iaas Saas, Paas 중 어떤 것이 더 효율적인 서비스가 될 것인지. 이러한 점을 반드시 숙지하고 고객에게 제공해야 할 것



```
삼성전자 청년 소프트웨어 교육을 통해 신입 개발자로 꿈을 키워 나가며 어떤 개발자가 될 것인가에 대한 많은 생각을 하였습니다. IT 기술을 배우며 제가 원하는 개발자의 모습은 "새로운 기술을 통해 기존 산업의 비효율을 효율적으로 바꾸는 것"입니다. 효성 ITX는 이러한 제 생각을 실현 시킬 수 있는 곳이라 생각하여 지원하였습니다. 기존의 서비스 방식을 통합한 unified 방식을 사용하기에 다양한 업무를 진행하며 다양한 산업에 이를 활용할 수 있을 것입니다.
무엇보다 업무를 통해 저와 고객, 모두에게 긍정적인 효과를 가져올 것입니다. 
우선 기존의 근무자들에겐 더 나은 근무환경을 줄 것입니다. 현재와 같이 코로나로 인한 상황에서 안전하게 자택근무 환경을 제공해주고, 고객들과 더 다양한 채널로 접근해 더 효율적으로 업무를 진행할 수 있게 할 것입니다. 고객의 경우 전화를 넘어 더 다양한 방법으로 접근할 수 있는 환경을 제공할 것입니다. 저 자신에겐 다양한 고객들에게 기술을 적용시키며 개발자로 더 성장할 수 있는 기회가 될 것입니다.
이처럼 효성ITX의 클라우드 서비스는 제가 생각하는 개발자의 역할을 모두 이룰 수 있는 기회를 줄 것입니다. 고객에겐 더 나은 근무환경을, 스스로는 더 나은 개발자, 사원으로 성장하기위해 지원하였습니다. 
```

```
삼성전자 청년 소프트웨어 교육을 통해 신입 개발자로 꿈을 키워나가며 어떤 개발자가 될 것인가에 대해 많은 생각을 하였습니다. IT 기술을 공부하며 저 스스로 내린 개발자의 모습은 "새로운 기술을 통해 기존 산업의 비효율을 효율적으로 바꾸는 것"이며 저 역시 그러한 개발자가 되기 위해 노력했습니다. 효성ITX의 사업, 기술은 제가 가진 이 생각을 실현할 수 있는 곳이라 생각하여 지원하였습니다.
우선 고객에겐 더 나은 환경을 제공할 수 있을 것입니다. 현재와 같이 코로나로 인한 상황에서 안전하게 자택근무 환경을 제공해주고, 단순히 전화만이 아닌 메일, 메시지, 웹 등 다양한 채널을 제공해 더 효율적으로 업무를 진행할 수 있을 것입니다.
저 스스로에겐 클라우드라는 기술에 대한 이해와 함께 다양한 산업의 고객들을 만나 기술을 적용하며 그 활용도와 이해를 더 깊게 해줄 것입니다. 단순히 개발자라는 직업을 주는 것이 아니라 이를 적용하고 활용할 수 있는 개발자로 성장할 기회일 것입니다.
이처럼 효성ITX의 클라우드 서비스는 제가 생각하는 개발자의 역할을 모두 이룰 기회를 줄 것입니다. 고객에겐 더 나은 근무환경을, 스스로는 더 나은 개발자, 사원으로 성장하기 위해 지원하였습니다. 

```



## 면접 질문 예상

1. 잘할수 있는것
2. 지원이유
3. 왜 IT로 공부를 시작했는지
4. 프로젝트하면서 힘들었던 것
5. 팀워크?
6. 프로젝트에 관한 설명
7. 

