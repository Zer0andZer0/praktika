import requests
import json


def get_github_repo_info(repo_url):
    try:
        owner, repo_name = repo_url.replace("https://github.com/", "").split("/")[0:2]
        api_url = f"https://api.github.com/repos/{owner}/{repo_name}"
        response = requests.get(api_url)
        response.raise_for_status()
        repo_info = response.json()
        owner_info = repo_info.get("owner", {})

        return {
            'id': repo_info.get("id"),
            'name': repo_info.get("name"),
            'full_name': repo_info.get("full_name"),
            'owner_id': owner_info.get("id"),
            'owner_login': owner_info.get("login"),
            'owner_url': owner_info.get("url"),
            'created_at': repo_info.get("created_at"),
            'updated_at': repo_info.get("updated_at"),
            'pushed_at': repo_info.get("pushed_at"),
            'html_url': repo_info.get("html_url"),
            'description': repo_info.get("description"),
            'language': repo_info.get("language"),
            'forks_count': repo_info.get("forks_count"),
            'stargazers_count': repo_info.get("stargazers_count"),
            'watchers_count': repo_info.get("watchers_count"),
            'open_issues_count': repo_info.get("open_issues_count"),
        }

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    repo_url = "https://github.com/NixOS/nixpkgs"
    repo_data = get_github_repo_info(repo_url)
    if repo_data:
        print(json.dumps(repo_data, indent=4))


