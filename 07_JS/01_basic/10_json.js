//Javascript object notation : JS의 Object처럼 표기하는 방법

const rawJson = `
    {
        "name":"kee",
        "job":"none"
    }
`


const parseData = JSON.parse(rawJson);

const bactTOJSON = JSON.stringify(parseData)

