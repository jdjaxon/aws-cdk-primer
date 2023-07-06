# aws-cdk-primer
Sandbox to learn how to use AWS services, SDK, and CDK.

## Cloud Development Kit (CDK)

### Prerequisites
All developers, regardless of language, will need
[Node.js](https://nodejs.org/en/download) 14.15.0 or later.

#### Python
- Python 3.7 or later including `pip` and `virtualenv`
##### Install
```
python -m pip install aws-cdk-lib
```
##### Import
```python
import aws-cdk as cdk
```
---

#### Javascript
- No additional requirements
##### Install
```
npm install aws-cdk-lib
```
##### Import
```javascript
const cdk = require('aws-cdk-lib');
```
---

#### Typescript
TypeScript 3.8 or later (`npm -g install typescript`)
##### Install
```
npm install aws-cdk-lib
```
##### Import
```typescript
import * as cdk from 'aws-cdk-lib';
```
---

#### Go
- Go 1.1.8 or later.
##### Install
```
go get github.com/aws/aws-cdk-go/awscdk/v2
```
##### Import
```go
import (
  "github.com/aws/aws-cdk-go/awscdk/v2"
)
```
---


## References
- CDK
    - https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html
