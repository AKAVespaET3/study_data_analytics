<details>
<summary>Titanic From Disaster</summary>

#### DDA

| Variable | Definition | Key | 분석가 의견 |
|-- | -- | -- | -- |
| survival | Survival | 0 = No, 1 = Yes | 범주형, 확인 결과 데이터 타입이 결정됨. |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형, 수치값으로 해석되지 않고 등급을 나타내기 때문, 객실 등급 별로 살아남은 사람들 분석가능  |
| sex | Sex | | 남자 여자 별로 살아남은 사람 분석 가능 | 범주형, 수치값으로 해석되지 않고 등급을 나타내기 때문 |
| Age | Age in years | 22.0, 38.0, 26.0, 35.0 | 수치형, 나이대 별로 살아남은 사람 분석 가능 |
| sibsp | # of siblings / spouses aboard the Titanic | 1, 1, 0, 1, 0 | 숫자형, 형제자매/배우자의 수를 정수 값으로 수치형 데이터 타입 |
| parch | # of parents / children aboard the Titanic | 0, 0, 0, 0, 0, | 숫자형, 부모/자녀의 수를 정수 값으로 나타냄 수치형 데이터 타입 |
| ticket | Ticket number | A/5 21171, PC 17599, STON/O2. 3101282 | 범주형 데이터 타입에 해당함 |
| fare | Passenger fare | 7.2500, 71.2833, 7.9250, | 지불한 요금을 나타냄 수치형 데이터 타입 |
| cabin | Cabin number |NaN, C85, NaN, C123 | 객실 번호를 나타내기 위한 문자열 범주형 데이터 타입 |
| embarked | Port of Embarkation | C = Cherbourg, Q = Queenstown, S = Southampton | 승객이 탑승한 항구를 나타내기 위한 문자열 범주형 데이터 타입|

</details>

<details>

<summary>TypeOfContractChannel</summary>

#### DDA

| Variable | Definition | Key | 분석가 의견 |
|-- | -- | -- | -- |
| id | 각 레코드의 고유 식별자 | --- | unique id의 경우 데이터로 사용 불가 판단 |
| type_of_contract  | 계약 유형 | 렌탈,멤버쉽 | 범주형(명목형), 각 계약 유형사이의 순서의 정보가 없음으로 명목형 |
| type_of_contract2| 다른 유형의 계약| Normal, TAS.. | 범주형(명목형), 명확한 순서가 나타나있지 않기때문에 명목형 |
| channel | 계약을 획득한 경로 | 서비스 방문, 홈쇼핑/방송 | 범주형(명목형), 서로 비교할 수 없는 의미적인 관계이기에 명목형 |
| datetime  | 레코드의 날짜와 시간 | --- | 수치형(연속형), 날짜이기 때문에 연속형으로 판단됨|
| Term | 계약 기간 | --- | 수치형(연속형) |
| payment_type | 지불 방식 | CMS,카드,이체.. | 범주형(명목형) |
| product | 계약과 관련된 제품 | K1,K2,K3.. | 범주형(명목형), 각 제품 유형은 서로 다른 범주로 분류, 서로 비교 할 수 없는 의미적 관계 |
| amount | 	계약과 관련된 금액 | --- | 수치형(이산형)|
| state | 계약의 주 또는 지역 | 계약확정, 해약확정 | 범주형(명목형) |
| overdue_count | 계약이 연체된 횟수 | 0, 1 | 수치형(이산형), 연체된 횟수를 파악해야 함|
| overdue | 현재 계약이 연체 중인지 여부 | 있음, 없음 | 	범주형(명목형), 연체 여부의 유무만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음 |
| credit rating | 고객의 신용 등급 | 9, 2, 8.. | 범주형(명목형), 데이터 확인결과 연산이 가능한 의미적인 순서가 아니기에 순서가 의미 없는 명목형 데이터 |
| bank | 계약과 연관된 은행 | --- | 범주형(명목형) |
| cancellation | 계약이 취소되었는지 여부 | --- | 범주형(명목형), 취소 여부만을 나타내기 때문에 비교 가능한 의미적인 순서가 없음 |
| age | 고객의 나이 | --- | 	수치형(이산형) |
| Mileage | 계약과 연관된 주행 거리 | --- | 수치형(연속형), 주행거리는 연속적인 데이터를 갖음 |


</details>
