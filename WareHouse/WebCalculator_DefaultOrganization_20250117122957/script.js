'''
This JavaScript file contains the logic for handling calculator operations and updating the display.
'''
document.addEventListener('DOMContentLoaded', (event) => {
    let currentOperand = '';
    let previousOperand = '';
    let operation = undefined;
    const displayElement = document.getElementById('display');
    function clearDisplay() {
        currentOperand = '';
        previousOperand = '';
        operation = undefined;
        updateDisplay();
    }
    function appendNumber(number) {
        if (number === '0' && currentOperand === '0') return;
        currentOperand = currentOperand.toString() + number.toString();
        updateDisplay();
    }
    function chooseOperation(op) {
        if (currentOperand === '') return;
        if (previousOperand !== '') {
            compute();
        }
        operation = op;
        previousOperand = currentOperand;
        currentOperand = '';
    }
    function compute() {
        let computation;
        const prev = parseFloat(previousOperand);
        const current = parseFloat(currentOperand);
        if (isNaN(prev) || isNaN(current)) return;
        switch (operation) {
            case '+':
                computation = prev + current;
                break;
            case '-':
                computation = prev - current;
                break;
            case '*':
                computation = prev * current;
                break;
            case '/':
                if (current === 0) {
                    alert("Cannot divide by zero");
                    return;
                }
                computation = prev / current;
                break;
            default:
                return;
        }
        currentOperand = computation;
        operation = undefined;
        previousOperand = '';
        updateDisplay();
    }
    function updateDisplay() {
        displayElement.innerText = currentOperand;
    }
    clearDisplay();
});