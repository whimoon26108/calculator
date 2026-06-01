import streamlit as st
import math

st.set_page_config(
    page_title="다기능 계산기",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 다기능 계산기 웹앱")
st.write("사칙연산, 모듈러 연산, 지수 연산, 로그 연산을 수행할 수 있는 계산기입니다.")

st.divider()

operation = st.selectbox(
    "계산할 연산을 선택하세요.",
    [
        "사칙연산",
        "모듈러 연산",
        "지수 연산",
        "로그 연산"
    ]
)

# -----------------------------
# 1. 사칙연산
# -----------------------------
if operation == "사칙연산":
    st.subheader("사칙연산")

    num1 = st.number_input("첫 번째 숫자를 입력하세요.", value=0.0)
    operator = st.selectbox("연산자를 선택하세요.", ["+", "-", "×", "÷"])
    num2 = st.number_input("두 번째 숫자를 입력하세요.", value=0.0)

    if st.button("계산하기"):
        if operator == "+":
            result = num1 + num2
            st.success(f"{num1} + {num2} = {result}")

        elif operator == "-":
            result = num1 - num2
            st.success(f"{num1} - {num2} = {result}")

        elif operator == "×":
            result = num1 * num2
            st.success(f"{num1} × {num2} = {result}")

        elif operator == "÷":
            if num2 == 0:
                st.error("0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                st.success(f"{num1} ÷ {num2} = {result}")


# -----------------------------
# 2. 모듈러 연산
# -----------------------------
elif operation == "모듈러 연산":
    st.subheader("모듈러 연산")
    st.write("모듈러 연산은 나눗셈의 나머지를 구하는 연산입니다.")

    num1 = st.number_input("나누어지는 수를 입력하세요.", value=0)
    num2 = st.number_input("나누는 수를 입력하세요.", value=1)

    if st.button("계산하기"):
        if num2 == 0:
            st.error("0으로 나눌 수 없습니다.")
        else:
            result = num1 % num2
            st.success(f"{num1} % {num2} = {result}")


# -----------------------------
# 3. 지수 연산
# -----------------------------
elif operation == "지수 연산":
    st.subheader("지수 연산")
    st.write("지수 연산은 어떤 수를 거듭제곱하는 연산입니다.")

    base = st.number_input("밑을 입력하세요.", value=2.0)
    exponent = st.number_input("지수를 입력하세요.", value=3.0)

    if st.button("계산하기"):
        result = base ** exponent
        st.success(f"{base}^{exponent} = {result}")


# -----------------------------
# 4. 로그 연산
# -----------------------------
elif operation == "로그 연산":
    st.subheader("로그 연산")
    st.write("로그 연산은 지수 연산의 반대 개념입니다.")

    log_type = st.selectbox(
        "로그 종류를 선택하세요.",
        [
            "일반 로그 log_a(x)",
            "자연로그 ln(x)",
            "상용로그 log10(x)"
        ]
    )

    if log_type == "일반 로그 log_a(x)":
        base = st.number_input("로그의 밑 a를 입력하세요.", value=2.0)
        x = st.number_input("진수 x를 입력하세요.", value=8.0)

        if st.button("계산하기"):
            if base <= 0:
                st.error("로그의 밑은 0보다 커야 합니다.")
            elif base == 1:
                st.error("로그의 밑은 1이 될 수 없습니다.")
            elif x <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
            else:
                result = math.log(x, base)
                st.success(f"log_{base}({x}) = {result}")

    elif log_type == "자연로그 ln(x)":
        x = st.number_input("진수 x를 입력하세요.", value=1.0)

        if st.button("계산하기"):
            if x <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
            else:
                result = math.log(x)
                st.success(f"ln({x}) = {result}")

    elif log_type == "상용로그 log10(x)":
        x = st.number_input("진수 x를 입력하세요.", value=10.0)

        if st.button("계산하기"):
            if x <= 0:
                st.error("로그의 진수는 0보다 커야 합니다.")
            else:
                result = math.log10(x)
                st.success(f"log10({x}) = {result}")

st.divider()

st.caption("Made with Python & Streamlit")
