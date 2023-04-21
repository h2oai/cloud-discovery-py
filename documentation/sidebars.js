module.exports = {
  defaultSidebar: [
    "index",
    {
      type: 'doc',
      id: 'overview',
    },
    {
      "Examples": [
        {
          type: 'autogenerated',
          dirName: 'examples',
        },
      ],
    },
    {
      type: "category",
      label: "API Reference",
      link: {
        type: 'generated-index',
        title: 'API',
        slug: '/api',
      },
      items: [
        {
          type: 'doc',
          id: 'api/h2o_discovery/h2o_discovery',
        },
        {
          type: 'doc',
          id: 'api/h2o_discovery/model',
        },
      ]
    },
    {
      type: 'doc',
      id: 'release-notes',
    },

  ],
};
