# cloudage

Small tool to create Graphviz representation of an AWS Cloudformation template.
It allows seeing how resources `Ref` each other and also where parameters are
used.

Install via pip:

```bash
pip install cloudage
```

And pass template JSON via stdin:

```bash
cloudage <mytemplate.json >output.dot
```
