import os
import glob


def custom_sort(rank):
    order = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Ruby"]
    if rank in order:
        return order.index(rank)
    else:
        return rank


def count_readme_files(directory):
    os.chdir(directory)
    readme_files = glob.glob("**/README.md", recursive=True)
    os.chdir("..")
    return len(readme_files)


def main():
    root_dir = os.getcwd()
    readme_counts = {}
    total_count = 0

    os.chdir(root_dir)
    sites = sorted(
        [d for d in os.listdir() if os.path.isdir(d) and d not in [".git", ".github"]]
    )

    for site in sites:
        site_path = os.path.join(root_dir, site)
        os.chdir(site_path)
        ranks = sorted([d for d in os.listdir() if os.path.isdir(d)], key=custom_sort)
        total_site = 0

        for rank in ranks:
            rank_path = os.path.join(site_path, rank)
            count = count_readme_files(rank_path)
            readme_counts[f"{site}/{rank}"] = count
            total_site += count

        readme_counts[f"{site}/total"] = total_site
        total_count += total_site
        os.chdir(root_dir)

    readme_counts["total"] = total_count

    with open("README.md", "w") as readme_file:
        readme_file.write("# 프로그래머스, 백준 문제풀이를 정리한 레포지토리 입니다. \n\n")
        for key, value in readme_counts.items():
            if "/total" in key:
                site_name = key.split("/")[0]
                readme_file.write(f"## {site_name}\n")
                for k, v in readme_counts.items():
                    if k.startswith(site_name) and "total" not in k:
                        rank_name = k.split("/")[1]
                        readme_file.write(f"- {rank_name}: {v}\n")
                readme_file.write(f"- total: {value}\n\n")

        readme_file.write("## Total\n")
        readme_file.write(f"- {total_count}\n")


if __name__ == "__main__":
    main()
