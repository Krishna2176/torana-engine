from torana import __version__


def main() -> None:
    print("=" * 50)
    print("TORANA Engine")
    print(f"Version : {__version__}")
    print("=" * 50)
    print()
    print("Bootstrap completed successfully.")
    print("Ready to initialize the Engine.")


if __name__ == "__main__":
    main()