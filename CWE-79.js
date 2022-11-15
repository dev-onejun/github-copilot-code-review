const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('Hello World!');
    }
);

// router which says hello to the user
app.get('/hello/:name', (req, res) => {
    res.send('Hello ' + req.params.name);
    }
);

// run server
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
    }
);


/***
 # example
 * http://localhost:3000/hello/<script>alert('hi')</script>
 # Result
 * cannot GET /hello/%3Cscript%3Ealert(%27hi%27)%3C/script%3E
 * http://localhost:3000/hello/%3Cscript%3Ealert('hi')%3C/script%3E
 */