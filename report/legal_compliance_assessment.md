# Task 3: Legal and Ethical Compliance Assessment

## 1. Scope and assumptions

SecureFinance Africa is a fictional platform initially intended for deployment in Nigeria. Its proposed functions include identity verification, fraud detection, and automated financial risk assessment. This assessment assumes that the platform may process personal and financial information. Biometric processing, creditworthiness assessment, and international data transfers must be confirmed against the final system design.

The assessment distinguishes binding legislation from non-binding ethical frameworks. It is an academic assessment and does not constitute legal advice.

## 2. Nigeria Data Protection Act 2023

The Nigeria Data Protection Act 2023 is central to the initial deployment because the platform will operate in Nigeria and process personal data.

Relevant requirements include:
- Section 24: principles governing personal-data processing.
- Section 25: lawful basis for processing.
- Sections 26-27: consent requirements and information to be provided to data subjects, as applicable.
- Section 28: Data Privacy Impact Assessment where processing is likely to result in high risk to rights and freedoms.
- Section 30: additional requirements relating to sensitive personal data.
- Sections 34-38: data-subject rights and related protections.
- Section 37: safeguards for decisions based solely on automated processing that produce legal or similarly significant effects.
- Section 39: security of personal data.
- Sections 41-43: requirements concerning transfers of personal data, as applicable.

Before deployment, SecureFinance Africa should document the lawful basis for each processing purpose, minimise data collection, provide appropriate privacy notices, establish retention limits, and implement security controls. It should assess whether a DPIA is required and complete it before relevant high-risk processing begins.

Where Section 37 applies, the organisation must assess the statutory conditions and exceptions and implement suitable safeguards. These include rights to human intervention, to express the data subject's point of view, and to contest the decision. The platform should provide a documented review and appeal process.

If biometric data is used, its classification and applicable legal conditions must be assessed before collection or processing. International hosting and third-party AI services must also be evaluated for applicable transfer requirements.

Evidence should include a data inventory, lawful-basis assessment, privacy notices, DPIA where required, data-subject request procedure, access-control reviews, security testing, incident-response procedures, vendor assessments, and transfer documentation where applicable.

## 3. EU Artificial Intelligence Act

The EU AI Act is binding legislation. Its applicability to SecureFinance Africa depends on territorial scope, the organisation's role, the intended purpose of each AI function, and the relevant provisions and dates of application.

The organisation should separately classify identity verification, fraud detection, and financial risk assessment. Under Annex III, point 5(b), AI used to evaluate the creditworthiness of natural persons or establish their credit score may be high-risk, subject to the regulation's provisions and exceptions. AI systems intended to be used exclusively to detect financial fraud are excluded from that particular category. Certain biometric uses are also treated differently; biometric verification solely intended to confirm a person's claimed identity is excluded from the remote-biometric-identification category described in Annex III, point 1(a).

If the Act applies and a function is high-risk, the organisation should assess relevant requirements for risk management, data governance, technical documentation, record-keeping, human oversight, accuracy, robustness, cybersecurity, quality management, and conformity assessment.

The organisation must verify the applicable implementation dates and current consolidated legislation before any deployment that may fall within EU jurisdiction.

## 4. UNESCO Recommendation on the Ethics of AI

UNESCO's 2021 Recommendation is a non-binding international ethical framework. It emphasises human rights and dignity, proportionality, prevention of harm, fairness, privacy, transparency, human oversight, safety, security, and accountability.

SecureFinance Africa should operationalise these principles through pre-deployment impact assessment, fairness testing across relevant groups, understandable explanations for consequential decisions, privacy-by-design, human review, and documented responsibility for AI lifecycle decisions.

## 5. OECD AI Principles

The OECD AI Principles are recommendations rather than directly binding legislation. The principles, updated in 2024, address inclusive growth and well-being; human rights, fairness, and privacy; transparency and explainability; robustness, security, and safety; and accountability.

The platform should translate these principles into measurable controls: group-based fairness metrics, model documentation, explainability evidence, adversarial security testing, performance monitoring, incident management, and clearly assigned risk owners.

## 6. Consolidated compliance matrix

| Framework | Binding status | Main concern | Proposed control | Evidence |
|---|---|---|---|---|
| Nigeria NDPA 2023 | Binding Nigerian legislation | Lawful and fair personal-data processing | Lawful-basis assessments, minimisation, privacy notices, retention controls | Data inventory, notices, processing records |
| Nigeria NDPA 2023 | Binding Nigerian legislation | High-risk processing and automated decisions | DPIA where required, human review, contest mechanisms | DPIA, review procedure, appeal records |
| Nigeria NDPA 2023 | Binding Nigerian legislation | Privacy and security | Access control, encryption, monitoring, incident response | Security tests, access logs, incident plan |
| EU AI Act | Binding where applicable | Classification and high-risk AI obligations | Classify each function; implement applicable lifecycle controls | Classification rationale, technical documentation |
| UNESCO Recommendation | Non-binding ethical framework | Human rights, fairness, privacy, oversight | Fairness testing, impact assessment, human review | Fairness reports, impact assessment, review logs |
| OECD AI Principles | Non-binding recommendation | Transparency, robustness, accountability | Explainability, security testing, assigned owners | Model documentation, test results, risk register |

## 7. Deployment implications

The platform should not be approved for production solely because a compliance matrix has been completed. Before launch, the organisation should verify the legal basis for all processing, assess the need for a DPIA, validate the system's intended purposes and jurisdictional scope, test fairness and security, implement meaningful human review, and retain evidence of control effectiveness.

Any unresolved critical risk, material unexplained disparity, serious security weakness, or missing legal safeguard should trigger escalation and may require postponing deployment.

## 8. Official references

1. Nigeria Data Protection Act 2023, Nigeria Data Protection Commission: https://ndpc.gov.ng/wp-content/uploads/2024/03/Nigeria_Data_Protection_Act_2023.pdf
2. Regulation (EU) 2024/1689, Artificial Intelligence Act, EUR-Lex: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
3. UNESCO, Recommendation on the Ethics of Artificial Intelligence: https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
4. OECD, Recommendation of the Council on Artificial Intelligence, OECD/LEGAL/0449: https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449
