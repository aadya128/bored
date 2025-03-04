from exa_py import Exa

exa = Exa('8292f7bd-146b-4c4d-9076-3e13435726ce')
query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.youtube.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()

print(response)

