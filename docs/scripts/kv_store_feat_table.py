import sys
from pathlib import Path

from langchain_community import document_loaders
from langchain_core.document_loaders.base import BaseLoader

KV_STORE_TEMPLATE = """\
---
sidebar_class_name: hidden
keywords: [compatibility]
custom_edit_url:
hide_table_of_contents: true
---

# Key-value stores

[Key-value stores](/docs/concepts/#key-value-stores) are used by other LangChain components to store and retrieve data.

:::info

If you'd like to contribute an integration, see [Contributing integrations](/docs/contributing/integrations/).

:::


## Features

The following table shows information on all available key-value stores.

{table}

"""

KV_STORE_FEAT_TABLE = {
    "AstraDBByteStore": {
        "class": "[AstraDBByteStore](https://api.python.langchain.com/en/latest/storage/langchain_astradb.storage.AstraDBByteStore.html)",
        "local": False,
        "package": "[langchain_astradb](https://api.python.langchain.com/en/latest/astradb_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_astradb?style=flat-square&label=%20)",
    },
    "CassandraByteStore": {
        "class": "[CassandraByteStore](https://api.python.langchain.com/en/latest/storage/langchain_community.storage.cassandra.CassandraByteStore.html)",
        "local": False,
        "package": "[langchain_community](https://api.python.langchain.com/en/latest/community_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_community?style=flat-square&label=%20)",
    },
    "ElasticsearchEmbeddingsCache": {
        "class": "[ElasticsearchEmbeddingsCache](https://api.python.langchain.com/en/latest/cache/langchain_elasticsearch.cache.ElasticsearchEmbeddingsCache.html)",
        "local": True,
        "package": "[langchain_elasticsearch](https://api.python.langchain.com/en/latest/elasticsearch_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_elasticsearch?style=flat-square&label=%20)",
    },
    "LocalFileStore": {
        "class": "[LocalFileStore](https://api.python.langchain.com/en/latest/storage/langchain.storage.file_system.LocalFileStore.html)",
        "local": True,
        "package": "[langchain](https://api.python.langchain.com/en/latest/langchain_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain?style=flat-square&label=%20)",
    },
    "InMemoryByteStore": {
        "class": "[InMemoryByteStore](https://api.python.langchain.com/en/latest/stores/langchain_core.stores.InMemoryByteStore.html)",
        "local": True,
        "package": "[langchain_core](https://api.python.langchain.com/en/latest/core_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_core?style=flat-square&label=%20)",
    },
    "RedisStore": {
        "class": "[RedisStore](https://api.python.langchain.com/en/latest/storage/langchain_community.storage.redis.RedisStore.html)",
        "local": True,
        "package": "[langchain_community](https://api.python.langchain.com/en/latest/community_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_community?style=flat-square&label=%20)",
    },
    "UpstashRedisByteStore": {
        "class": "[UpstashRedisByteStore](https://api.python.langchain.com/en/latest/storage/langchain_community.storage.upstash_redis.UpstashRedisByteStore.html)",
        "local": False,
        "package": "[langchain_community](https://api.python.langchain.com/en/latest/community_api_reference.html)",
        "downloads": "![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain_community?style=flat-square&label=%20)",
    },
}

DEPRECATED = []


def get_kv_store_table() -> str:
    """Get the table of KV stores."""

    header = ["name", "local", "package", "downloads"]
    title = ["Class", "Local", "Package", "Downloads"]
    rows = [title, [":-"] + [":-:"] * (len(title) - 1)]
    for loader, feats in sorted(KV_STORE_FEAT_TABLE.items()):
        if not feats or loader in DEPRECATED:
            continue
        rows += [
            [feats["class"]]
            + ["✅" if feats.get(h) else "❌" for h in header[1:2]]
            + [feats["package"], feats["downloads"]]
        ]
    return "\n".join(["|".join(row) for row in rows])


if __name__ == "__main__":
    output_dir = Path(sys.argv[1])
    output_integrations_dir = output_dir / "integrations"
    output_integrations_dir_kv_stores = output_integrations_dir / "stores"
    output_integrations_dir_kv_stores.mkdir(parents=True, exist_ok=True)

    kv_stores_page = KV_STORE_TEMPLATE.format(table=get_kv_store_table())
    with open(output_integrations_dir / "stores" / "index.mdx", "w") as f:
        f.write(kv_stores_page)
