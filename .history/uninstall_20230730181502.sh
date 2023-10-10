#!/bin/bash

# Color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
BRIGHT='\033[1m'
NC='\033[0m' # No Color
if [[ "$OSTYPE" == "darwin"* ]]; then   

    yes=("yes" "Yes" "YES")

    echo -e "${RED}${BRIGHT}!Are you sure you want to remove your Packages (YES/NO)!: ${NC}"

    read -p ">>> " YES_NO

    if [[ "${yes[*]}" == *"$YES_NO"* ]]; then
        if ping -q -c 1 -W 1 google.com >/dev/null; then # checks if the user is connected to the internet
            # Packages to check for installation
            Packages=(
                "wget"
                "hydra"
                "nmap"
                "mysql"
                "figlet"
            )

            # PIP packages that will be uninstalled if they are installed
            pipPackages=(
                "tqdm"
                "asyncio"
                "colorama"
            )

            # Check package installation
            check_package() {
                package_name="$1"
                if command -v "$package_name" >/dev/null 2>&1; then
                    echo "$package_name is installed."
                    brew uninstall "$package_name"
                else
                    echo -e "${RED}$package_name${NC} is not installed."
                fi
            }

            # Check packages
            for package in "${Packages[@]}"
            do
                check_package "$package"
            done

            # Uninstall PIP packages
            for pipPackage in "${pipPackages[@]}"
            do
                if pip3 show "$pipPackage" >/dev/null 2>&1; then
                    pip3 uninstall "$pipPackage" -y

                    # Check the exit status of the last command
                    if [ $? -ne 0 ]; then
                        echo -e "Error occurred during uninstallation of \"$pipPackage\""
                        exit 1
                    else
                        echo -e "${pipPackage}: uninstalled ${GREEN}successfully${NC}"
                    fi
                else
                    echo -e "${RED}${pipPackage}${NC}: is not installed"
                fi
            done

            pip3 uninstall -y pip

            # Check the exit status of the last command
            if [ $? -ne 0 ]; then
                echo -e "The packages that are removed are: ${GREEN}"
                for package in "${Packages[@]}"
                    do
                        echo -e "$package"
                done
                echo -e "________PIP Packages________"
                for pipPackage in "${pipPackages[@]}"
                    do
                        echo -e "$pipPackage"
                done
                echo -e "________ERROR________"
                echo -e "${RED}Error occurred during pip uninstallation${NC}"
            else
                echo -e "pip: uninstalled ${GREEN}successfully${NC}"
                echo -e "The packages that are removed are: ${GREEN}"
                for package in "${Packages[@]}"
                    do
                        echo -e "$package"
                done
                echo -e "________PIP Packages________"
                for pipPackage in "${pipPackages[@]}"
                    do
                        echo -e "$pipPackage"
                done
            fi

        else
            echo -e "${RED}ERROR NOT CONNECTED TO THE INTERNET${NC}"
        fi

    else
        echo -e "Ok, I will not remove the packages."
    fi
else
    echo "Wrong OS please use the correct OS." #if the users is not useing the right OS it says "You are useing the wrong OS"
fi