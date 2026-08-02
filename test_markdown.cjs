const { unified } = require('unified');
const remarkParse = require('remark-parse');
const remarkRehype = require('remark-rehype');
const rehypeStringify = require('rehype-stringify');

const markdown = `*For questions* **21** *to* **26**, *choose the correct alternative to fill in the blank spaces.*`;

unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypeStringify)
  .process(markdown)
  .then((file) => console.log(String(file)));
