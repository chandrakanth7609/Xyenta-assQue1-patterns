let display = document.getElementById("display");
let isOperatorClicked = false;
let firstOperand = null;
let operator = null;

function appendToDisplay(value) {
    if (isOperatorClicked && "+-*/".includes(value)) {
        return;
    }
    if (isOperatorClicked) {
        display.value = value;
    } else {
        display.value += value;
    }
    isOperatorClicked = "+-*/".includes(value);
}

function clearDisplay() {
    display.value = "";
    isOperatorClicked = false;
    firstOperand = null;
    operator = null;
}

function setOperator(selectedOperator) {
    if (firstOperand === null) {
        firstOperand = parseFloat(display.value);
        operator = selectedOperator;
        isOperatorClicked = true;
    } else {
        const secondOperand = parseFloat(display.value);
        firstOperand = calculateResult(firstOperand, secondOperand, operator);
        display.value = firstOperand;
        operator = selectedOperator;
        isOperatorClicked = true;
    }
}

function calculateResult(a, b, op) {
    switch (op) {
        case "+":
            return a + b;
        case "-":
            return a - b;
        case "*":
            return a * b;
        case "/":
            if (b === 0) {
                return "Error";
            }
            return a / b;
        default:
            return "Error";
    }
}
