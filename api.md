# API

## V1

### Contracts

#### Audit

Types:

```python
from formalize.types.api.v1.contracts import AuditCreateResponse, AuditBatchResponse
```

Methods:

- <code title="post /api/v1/contracts/{contract_id}/audit">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">create</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_create_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_create_response.py">AuditCreateResponse</a></code>
- <code title="post /api/v1/contracts/{contract_id}/audit/batch">client.api.v1.contracts.audit.<a href="./src/formalize/resources/api/v1/contracts/audit.py">batch</a>(contract_id, \*\*<a href="src/formalize/types/api/v1/contracts/audit_batch_params.py">params</a>) -> <a href="./src/formalize/types/api/v1/contracts/audit_batch_response.py">AuditBatchResponse</a></code>
