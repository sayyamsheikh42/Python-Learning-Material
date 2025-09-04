# Topic 4: Object-Oriented Programming (OOP) - Flow Diagram

```mermaid
flowchart TD
    A[Start OOP Design] --> B[Define Class Blueprint]
    B --> C[Class: Book]
    
    C --> D[Attributes<br/>Data Storage]
    D --> E[title: str]
    D --> F[author: str]
    D --> G[pages: int]
    D --> H[is_checked_out: bool]
    
    C --> I[Methods<br/>Functions/Actions]
    I --> J[__init__<br/>Constructor]
    I --> K[check_out<br/>Borrow book]
    I --> L[return_book<br/>Return book]
    I --> M[get_info<br/>Display info]
    
    J --> N[Initialize Object]
    N --> O[Create Book Instance]
    O --> P[book1 = Book<br/>'Python Programming'<br/>'Guido van Rossum'<br/>300]
    
    P --> Q[Object Operations]
    Q --> R[book1.check_out]
    Q --> S[book1.return_book]
    Q --> T[book1.get_info]
    
    R --> U{Book Available?}
    U -->|Yes| V[Mark as Checked Out<br/>Return Success Message]
    U -->|No| W[Return Already Checked Out Message]
    
    S --> X{Book Checked Out?}
    X -->|Yes| Y[Mark as Available<br/>Return Success Message]
    X -->|No| Z[Return Not Checked Out Message]
    
    T --> AA[Return Book Information<br/>Title, Author, Pages, Status]
    
    V --> BB[Library Management]
    W --> BB
    Y --> BB
    Z --> BB
    AA --> BB
    
    BB --> CC[Library Class]
    CC --> DD[Encapsulation<br/>Private Attributes]
    DD --> EE[_books: list<br/>Private attribute]
    
    CC --> FF[Library Methods]
    FF --> GG[add_book<br/>Add to collection]
    FF --> HH[find_book<br/>Search by title]
    FF --> II[get_available_books<br/>Filter available]
    FF --> JJ[get_library_info<br/>Generate report]
    
    GG --> KK[Add Book to Library]
    HH --> LL[Search Book Collection]
    II --> MM[Filter Available Books]
    JJ --> NN[Generate Statistics]
    
    KK --> OO[Library Operations]
    LL --> OO
    MM --> OO
    NN --> OO
    
    OO --> PP[OOP Principles]
    PP --> QQ[Encapsulation<br/>Data + Methods together]
    PP --> RR[Inheritance<br/>Create new classes from existing]
    PP --> SS[Polymorphism<br/>Same interface, different behavior]
    
    TT[OOP Benefits] --> UU[Organization<br/>Code structure]
    TT --> VV[Reusability<br/>Use classes multiple times]
    TT --> WW[Modularity<br/>Independent development]
    TT --> XX[Maintainability<br/>Easy to modify]
    
    style A fill:#e1f5fe
    style C fill:#fff3e0
    style P fill:#e8f5e8
    style BB fill:#f3e5f5
    style PP fill:#e0f2f1
    style TT fill:#fce4ec
```

## Key Concepts Visualized:

1. **Class Definition**: Blueprint for creating objects with attributes and methods
2. **Object Creation**: Instantiating classes to create specific objects
3. **Encapsulation**: Keeping data and methods together, hiding internal details
4. **Object Operations**: Methods that manipulate object state
5. **OOP Principles**: Encapsulation, inheritance, and polymorphism
6. **Benefits**: Organization, reusability, modularity, and maintainability
