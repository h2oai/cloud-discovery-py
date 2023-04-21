# `h2o-cloud-discovery` Documentation

This is the documentation for the `h2o-cloud-discovery` library.
It's partially generated from the source code, and partially written by hand.

To generate the API docs that resist in the `/api` folder, run the following command:

```sh
hatch docs:generate
```

## Running this site

This site was generated using Makersaurus, which is a very thin wrapper around Facebook's Docusaurus. You can write documentation in the typical way, using markdown files located in the `docs` folder and registering those files in `sidebars.js`.

Use the following commands to run the generate the site and run it locally:

```
npx @h2oai/makersaurus@latest gen
cd gen
npm install
npm start
```

## More information

Use the Makersaurus docs to earn how to edit docs, deploy the site, set up versioning and more.
