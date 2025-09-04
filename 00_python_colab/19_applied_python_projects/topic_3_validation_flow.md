# Topic 3: Data Validation - Flow Diagram

```mermaid
flowchart TD
    A[Start Data Validation] --> B[Receive Input Data]
    B --> C{Validation Approach}
    
    C -->|Dataclasses| D[Create @dataclass]
    C -->|Pydantic| E[Create BaseModel]
    C -->|Custom| F[Write Custom Functions]
    
    D --> G[Define __post_init__]
    G --> H[Validate Name]
    G --> I[Validate Email]
    G --> J[Validate Age]
    
    E --> K[Use Field Validators]
    K --> L[Type Validation]
    K --> M[Format Validation]
    K --> N[Range Validation]
    
    F --> O[Manual Validation Logic]
    O --> P[Check Data Types]
    O --> Q[Check Data Format]
    O --> R[Check Data Range]
    
    H --> S{Name Valid?}
    I --> T{Email Valid?}
    J --> U{Age Valid?}
    
    L --> V{Type Valid?}
    M --> W{Format Valid?}
    N --> X{Range Valid?}
    
    P --> Y{Type Check Pass?}
    Q --> Z{Format Check Pass?}
    R --> AA{Range Check Pass?}
    
    S -->|No| BB[Raise ValueError<br/>Name too short]
    T -->|No| CC[Raise ValueError<br/>Invalid email format]
    U -->|No| DD[Raise ValueError<br/>Age out of range]
    
    V -->|No| EE[Pydantic ValidationError]
    W -->|No| EE
    X -->|No| EE
    
    Y -->|No| FF[Custom Validation Error]
    Z -->|No| FF
    AA -->|No| FF
    
    S -->|Yes| GG[Validation Passed]
    T -->|Yes| GG
    J -->|Yes| GG
    
    V -->|Yes| HH[Pydantic Success]
    W -->|Yes| HH
    N -->|Yes| HH
    
    Y -->|Yes| II[Custom Success]
    Z -->|Yes| II
    AA -->|Yes| II
    
    GG --> JJ[Object Created Successfully]
    HH --> JJ
    II --> JJ
    
    BB --> KK[Error Handling]
    CC --> KK
    DD --> KK
    EE --> KK
    FF --> KK
    
    JJ --> LL[Process Valid Data]
    KK --> MM[Display Error Message]
    
    LL --> NN[End Validation]
    MM --> NN
    
    OO[Validation Types] --> PP[Type Validation<br/>Check data types]
    OO --> QQ[Format Validation<br/>Check patterns]
    OO --> RR[Range Validation<br/>Check limits]
    OO --> SS[Required Fields<br/>Check presence]
    
    TT[Why Validate?] --> UU[Prevent Errors<br/>Catch problems early]
    TT --> VV[Data Quality<br/>Ensure accuracy]
    TT --> WW[Security<br/>Protect against attacks]
    TT --> XX[User Experience<br/>Clear error messages]
    
    style A fill:#e1f5fe
    style NN fill:#c8e6c9
    style BB fill:#ffcdd2
    style CC fill:#ffcdd2
    style DD fill:#ffcdd2
    style EE fill:#ffcdd2
    style FF fill:#ffcdd2
    style JJ fill:#c8e6c9
    style OO fill:#f3e5f5
    style TT fill:#e0f2f1
```

## Key Concepts Visualized:

1. **Validation Approaches**: Dataclasses, Pydantic, and custom validation
2. **Validation Types**: Type, format, range, and required field validation
3. **Error Handling**: Different ways to handle validation failures
4. **Benefits**: Why validation is important for data quality and security
5. **Success Flow**: How valid data proceeds through the system
