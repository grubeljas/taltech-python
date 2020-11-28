"""."""
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle


def get_links_from_spreadsheet(id: str, token: str) -> list:
    """Should get a list of strings from the first column of a Google Spreadsheet with the given ID."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as tok:
            creds = pickle.load(tok)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', ['https://www.googleapis.com/auth/spreadsheets.readonly'])
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as tok:
            pickle.dump(creds, tok)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=id,
                                range='A1:A100').execute()
    values = result.get('values', [])
    links = []
    for value in values:
        links.append(value[0])
    return links


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """Should get a list of links to songs in the Youtube playlist with the given address."""
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    creds = None
    if os.path.exists('tok.pickle'):
        with open('tok.pickle', 'rb') as tok:
            creds = pickle.load(tok)
        # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                developer_key, ["https://www.googleapis.com/auth/youtube.readonly"])
            creds = flow.run_local_server(port=0)
            creds = flow.run_console()
        # Save the credentials for the next run
        with open('tok.pickle', 'wb') as tok:
            pickle.dump(creds, tok)
    # Get credentials and create an API client

    youtube = build(
        api_service_name, api_version, credentials=creds)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=25,
        playlistId=link
    )
    response = request.execute()
    links = []
    i = 1
    for video in response['items']:
        plid = video["snippet"]["playlistId"]
        vid = video["contentDetails"]["videoId"]
        link = f'https://www.youtube.com/watch?v={vid}&list={plid}&index={i}&ab_channel={video["snippet"]["channelId"]}'
        links.append(link)
        i += 1
    return links


if __name__ == '__main__':
    id = '1l2r7lFeKavPCmOkn-6Lf2ttPKB6By6uCeDK44ZftJL4'
    token = 'sheer'
    print(get_links_from_playlist('PLt2aVE6fZ9_BHlRFemMH4w3TIXzpinO3C', 'credentials.json'))
