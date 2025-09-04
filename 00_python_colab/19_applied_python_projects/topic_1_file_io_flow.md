# Topic 1: File I/O and Text Processing - Flow Diagram

```mermaid
flowchart TD
    A[Start File I/O Process] --> B{File Operation Type}
    
    B -->|Read| C[Open File for Reading]
    B -->|Write| D[Open File for Writing]
    B -->|Append| E[Open File for Appending]
    
    C --> F[Use Context Manager<br/>with open()]
    D --> F
    E --> F
    
    F --> G{File Exists?}
    G -->|No| H[Handle File Not Found Error]
    G -->|Yes| I[Perform File Operation]
    
    I --> J{Operation Type}
    J -->|Read All| K[Read Entire File<br/>f.read()]
    J -->|Read Lines| L[Read Line by Line<br/>for line in f]
    J -->|Write Data| M[Write to File<br/>f.write()]
    
    K --> N[Process Text Data]
    L --> N
    M --> O[File Written Successfully]
    
    N --> P[Apply Text Processing]
    P --> Q[String Methods]
    Q --> R[.strip() - Remove whitespace]
    Q --> S[.split() - Split into parts]
    Q --> T[.replace() - Replace text]
    
    R --> U[Data Analysis]
    S --> U
    T --> U
    
    U --> V[Use Counter for Frequency]
    V --> W[Extract Information]
    W --> X[Generate Results]
    
    O --> Y[Close File Automatically]
    X --> Y
    H --> Z[Error Handling]
    
    Y --> AA[End Process]
    Z --> AA
    
    style A fill:#e1f5fe
    style AA fill:#c8e6c9
    style H fill:#ffcdd2
    style F fill:#fff3e0
    style P fill:#f3e5f5
```

## Key Concepts Visualized:

1. **File Operations**: Reading, writing, and appending to files
2. **Context Managers**: Automatic file handling with `with open()`
3. **Error Handling**: Managing file not found scenarios
4. **Text Processing**: String manipulation and data extraction
5. **Data Analysis**: Using Counter for frequency analysis
