UA_PADRAO = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36.'}

HEADER_LOGIN = {
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
  "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
  "cache-control": "max-age=0",
  "content-type": "application/x-www-form-urlencoded",
  "sec-fetch-dest": "document",
  "sec-fetch-mode": "navigate",
  "sec-fetch-site": "same-origin",
  "sec-fetch-user": "?1",
  "sec-gpc": "1",
  "referer": "https://suap.ifpb.edu.br/accounts/login/?next=/",
  "upgrade-insecure-requests": "1"
  }


REQ_JSON_LOGIN = {
  "referrer": "https://suap.ifpb.edu.br",
  "referrerPolicy": "same-origin",
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
  }


HEADER_BOLETIM = {
  "accept": "*/*",
  "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "sec-gpc": "1",
  "x-requested-with": "XMLHttpRequest"
}

REQ_JSON_BOLETIM = {
  "referrerPolicy": "same-origin",
  "method": "GET",
  "mode": "cors",
  "credentials": "include",
  "mode": "cors"
  }


