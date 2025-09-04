# Topic 2: Asynchronous Programming - Flow Diagram

```mermaid
flowchart TD
    A[Start Async Process] --> B{Programming Approach}
    
    B -->|Synchronous| C[Sequential Execution]
    B -->|Asynchronous| D[Concurrent Execution]
    
    C --> E[Task 1 Starts]
    E --> F[Task 1 Completes]
    F --> G[Task 2 Starts]
    G --> H[Task 2 Completes]
    H --> I[Task 3 Starts]
    I --> J[Task 3 Completes]
    J --> K[All Tasks Done<br/>Total Time: 3 seconds]
    
    D --> L[Define Async Function<br/>async def task_name]
    L --> M[Use asyncio.gather]
    M --> N[Task 1 Starts]
    M --> O[Task 2 Starts]
    M --> P[Task 3 Starts]
    
    N --> Q[Task 1 Completes]
    O --> R[Task 2 Completes]
    P --> S[Task 3 Completes]
    
    Q --> T[All Tasks Done<br/>Total Time: 1 second]
    R --> T
    S --> T
    
    T --> U[Performance Comparison]
    K --> U
    
    U --> V[Async is 3x Faster!]
    
    W[Async Syntax Elements] --> X[async def - Define async function]
    W --> Y[await - Wait for async operation]
    W --> Z[asyncio.run - Start event loop]
    W --> AA[asyncio.gather - Run tasks concurrently]
    W --> BB[asyncio.sleep - Non-blocking delay]
    
    CC[When to Use Async] --> DD[I/O Operations<br/>Network requests, file reading]
    CC --> EE[Multiple Tasks<br/>Several operations at once]
    CC --> FF[Waiting Time<br/>Operations with delays]
    
    style A fill:#e1f5fe
    style V fill:#c8e6c9
    style C fill:#ffecb3
    style D fill:#e8f5e8
    style K fill:#ffcdd2
    style T fill:#c8e6c9
    style W fill:#f3e5f5
    style CC fill:#e0f2f1
```

## Key Concepts Visualized:

1. **Synchronous vs Asynchronous**: Sequential vs concurrent execution
2. **Performance Benefits**: Async can be 3x faster for I/O operations
3. **Async Syntax**: Key elements like `async def`, `await`, `asyncio.gather`
4. **Use Cases**: When to choose async programming
5. **Event Loop**: How asyncio manages concurrent operations
