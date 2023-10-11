import concurrent.futures
import spider

# craw
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(spider.craw, spider.urls)
    htmls = list(zip(spider.urls, htmls))
    for url, html in htmls:
        print(url, len(html))

print("craw over")
# parse
with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(spider.parse, html)
        futures[future] = url

    # for future, url in futures.items():
    #     print(url, future.result())
    for future in concurrent.futures.as_completed(futures):
        url = futures[future]
        print(url, future.result())