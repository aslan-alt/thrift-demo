
exception InvalidaOperation {
    1: i32 whatOp,
    2: string why
}

enum Operation {
    ADD = 1,
    SUBTRACT = 2,
}

struct Work {
 1:i32 num1 =0,
 2:i32 num2,
 3:Operation op,
 4:optional string comment
}

service BasicService {
    // 返回值 ｜ 方法名 ｜ 参数 ｜ 异常
    double divide(1:i32 num1, 2:i32 num2) throws (1:InvalidaOperation e)
    oneway void ping()
}