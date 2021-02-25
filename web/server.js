import express from 'express';
import path from 'path';

/* Configuration */
const config = require(path.resolve(__dirname, 'config', 'public.config.json'));

/* Initialize the server */
const app = express();
app.use('/', express.static(path.resolve(__dirname, ...config.publish.expose)));

app.listen(config.publish.port, config.publish.host, () => {
    console.log(
        `Server listening on http://${config.publish.host}:${config.publish.port}.`
    );
});
