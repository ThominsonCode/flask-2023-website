const buttonAddQuestion = document.querySelector("#button_add_question")

buttonAddQuestion.addEventListener('click', function () {

    let idLastQuestion = this.parentNode.previousElementSibling.getAttribute('id').slice(-1)
    if (isNaN(idLastQuestion)) {
        idLastQuestion = 0
    }
    const idQuestion = Number(idLastQuestion) + 1
    this.parentNode.insertAdjacentElement('beforebegin', createQuestionBlock(idQuestion))
})

function selectOnChange(event) {
    let questionType = this.getAttribute('data-value')
    const new_questionType = this.value
    let answers = this.parentNode.nextElementSibling
    if ((new_questionType === 'radio' || new_questionType === 'checkbox') && (questionType !== 'radio' && questionType !== 'checkbox')) {
        answers.innerHTML = ``
        answers.append(createChoice(1, 1))
        answers.append(createChoice(1, 2))
        const button = createButtonForChoice(1)
        answers.append(button)
        button.addEventListener('click', buttonAddChoice)
    }
    if ((new_questionType === 'textfield' || new_questionType === 'textarea') && (questionType !== 'textfield' && questionType !== 'textarea')) {
        answers.innerHTML = ``
    }

    this.setAttribute('data-value', new_questionType)
}

function buttonAddChoice(event) {
    const nbChoix = this.parentNode.childElementCount - 1
    const idAnswer = nbChoix + 1
    this.insertAdjacentElement('beforebegin', createChoice(1, idAnswer))
}

function createQuestionBlock(idQuestion) {
    let fieldset = document.createElement('fieldset')
    fieldset.setAttribute('id', `fs_q_${idQuestion}`)
    fieldset.innerHTML = `<legend>Question ${idQuestion}</legend>

    <div id="q_${idQuestion}_text_block">
        <label for="q_${idQuestion}_text">Texte</label>
        <input type="text" name="q_${idQuestion}_text" id="q_${idQuestion}_text">
    </div>
    <div id="q_${idQuestion}_type_block">
        <label for="q_${idQuestion}_type">Type</label>
        <select name="q_${idQuestion}_type" id="q_${idQuestion}_type" data-value="empty">
            <option disabled selected>-- Selectionnez un type --</option>
            <option value="radio">Choix unique</option>
            <option value="checkbox">Choix multiple</option>
            <option value="textfield">Texte court</option>
            <option value="textarea">Texte long</option>
        </select>
    </div>
    <div id="q_${idQuestion}_answers">
    </div>`

    let select = fieldset.querySelector('select')
    select.addEventListener('change', selectOnChange)

    return fieldset
}

function createChoice(idQuestion, idAnswer) {
    const choice = document.createElement('p')
    choice.innerHTML = `
    <label for="q_${idQuestion}_a_${idAnswer}">Choix ${idAnswer}</label>
    <input type="text" name="q_${idQuestion}_a_${idAnswer}" id="q_${idQuestion}_a_${idAnswer}">
`;
    return choice
}

function createButtonForChoice(idQuestion) {
    const button = document.createElement('button')
    button.innerText = 'Ajouter un choix'
    button.setAttribute('type', 'button')
    button.setAttribute('id', `q_${idQuestion}_answers_add_choice`)
    return button;
}
