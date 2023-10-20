# OpenCRE SDK

[**OpenCRE**](https://github.com/OWASP/OpenCRE) is an interactive content linking platform and serves as a bridge, connecting various security standards and guidelines to present them in a unified, comprehensive view. By linking each section of a resource to a shared topic, known as a *Common Requirement (CRE)*, it ensures that users can access all related information from multiple sources in one place. 

The **OpenCRE SDK** is an essential toolkit for developers and contributors to this ecosystem. It empowers developers to:

- **Create** new Common Requirements.
- **Manage** and **retrieve** existing CREs.
- **Associate** various documents and external links to these CREs.

In essence, the OpenCRE SDK is a gateway for developers to interact with and expand the OpenCRE platform, making cybersecurity information more accessible and interconnected.

### Requirements

The OpenCRE SDK uses the requests library for HTTP communication with the OpenCRE platform. Ensure you've installed version 2.31.0, as detailed in `requirements.txt`.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/stateandprove/opencre-sdk.git
```

2. Navigate to the project directory:

```bash
cd opencre-sdk
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Initialize OpenCRE

```python
from opencre import OpenCRE

# Initialize OpenCRE SDK
opencre = OpenCRE()
```

### Retrieve a specific CRE by ID

```python
cre_id = "170-772"
cre = opencre.cre(cre_id)
print(str(cre))  # Outputs: 'CRE 170-772'
print(cre.name)  # Outputs: 'Cryptography'
print(cre.id)    # Outputs: '170-772'
```

### Access links of a CRE

```python
link = cre.links[5]
print(link.ltype)  # Outputs: 'Linked To'
doc = link.document
print(doc.name)   # Outputs: 'Cloud Controls Matrix'
```
#### Link Types (ltype)

`ltype` attribute in the `Link` class represents the type of relationship between the CRE and the linked document. Currently, there are two possible values for ltype:

- **`Contains`**: This indicates that the CRE ncludes the content of the linked document. For instance, a CRE about "Manual penetration testing" might contain another CRE about "Dynamic security testing".

- **`Linked To`**: This signifies a reference to an external standard, tool, or another CRE. For example, a CRE might be linked to a specific section in the "NIST SSDF" standard.

### Change SDK settings

The OpenCRE SDK settings are encapsulated within the `OpenCREConfig` dataclass. This dataclass provides default values for the `HOST_URL` and `API_PREFIX`, but you can modify them as needed.

1. View current settings:

```python
opencre.settings
# Output: OpenCREConfig(HOST_URL='https://www.opencre.org/', API_PREFIX='rest/v1/')
```

2. Access individual settings:

```python
opencre.settings.HOST_URL
# Output: 'https://www.opencre.org/'

opencre.settings.API_PREFIX
# Output: 'rest/v1/'
```

3. Modify a setting:

```python
opencre.settings.API_PREFIX = 'rest/v5'
opencre.settings.API_PREFIX
# Output: 'rest/v5/'
```

> :warning: **Warning:** Ensure that you modify the settings appropriately based on your requirements. Incorrect settings might lead to unexpected behavior or errors when interacting with the OpenCRE platform.

### Retrieve root CREs

```python
root_cres = opencre.root_cres()
for cre in root_cres:
    print(cre)
```

## Troubleshooting

If you encounter an error like `requests.exceptions.MissingSchema: Invalid URL`, ensure that the `HOST_URL` in the settings has the correct format, including the scheme (e.g., `https://`).

## Structure

- `opencre`: Main module containing the SDK's functionalities.
  - `__init__.py`: Initializes the OpenCRE SDK.
  - `models.py`: Contains the data models for CRE, Link, and various document types.
  - `opencre.py`: Core functionalities of the SDK, including API requests and CRE management.
- `.gitignore`: Specifies intentionally untracked files that Git should ignore.
- `requirements.txt`: Lists the required Python packages for the SDK.

## Contributing

We welcome contributions! Please submit pull requests for bug fixes, features, and improvements. See [**Contributing**](https://github.com/OWASP/OpenCRE/blob/main/CONTRIBUTING.md) for contributing instructions.
