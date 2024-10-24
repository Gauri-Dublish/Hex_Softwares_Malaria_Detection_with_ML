{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5QuuVwdjnXQL6rLRNQvf5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Gauri-Dublish/Hex_Softwares_Malaria_Detection_with_ML/blob/main/python_section_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XdPb2Mzk-gMa",
        "outputId": "a3e5259d-cb24-411b-a35f-a64fc919b851"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 2, 1, 6, 5, 4, 8, 7]\n",
            "[2, 1, 4, 3, 5]\n",
            "[40, 30, 20, 10, 70, 60, 50]\n"
          ]
        }
      ],
      "source": [
        "def reverse_by_n_elements(lst, n):\n",
        "    result = []   # This will hold our final output\n",
        "    for i in range(0, len(lst), n):\n",
        "        group = []\n",
        "        for j in range(min(n, len(lst) - i)):\n",
        "            group.append(lst[i + j])\n",
        "        result.extend(group[::-1])\n",
        "    return result\n",
        "\n",
        "# Examples\n",
        "print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]\n",
        "print(reverse_by_n_elements([1, 2, 3, 4, 5], 2))           # Output: [2, 1, 4, 3, 5]\n",
        "print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))  # Output: [40, 30, 20, 10, 70, 60, 50]\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def group_strings_by_length(strings):\n",
        "    length_dict = {}\n",
        "    for string in strings:\n",
        "        length = len(string)\n",
        "        if length not in length_dict:\n",
        "            length_dict[length] = []\n",
        "        length_dict[length].append(string)\n",
        "    return dict(sorted(length_dict.items()))\n",
        "\n",
        "# Examples\n",
        "print(group_strings_by_length([\"apple\", \"bat\", \"car\", \"elephant\", \"dog\", \"bear\"]))\n",
        "# Output: {3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}\n",
        "\n",
        "print(group_strings_by_length([\"one\", \"two\", \"three\", \"four\"]))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lz_4JIx-Bb0m",
        "outputId": "bf013b1c-5ba6-45d8-ee02-a1752564fdbd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}\n",
            "{3: ['one', 'two'], 4: ['four'], 5: ['three']}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def flatten_dict(d, parent_key='', sep='.'):\n",
        "    items = []\n",
        "    for k, v in d.items():\n",
        "        new_key = f\"{parent_key}{sep}{k}\" if parent_key else k\n",
        "        if isinstance(v, dict):\n",
        "            items.extend(flatten_dict(v, new_key, sep=sep).items())\n",
        "        elif isinstance(v, list):\n",
        "            for i, item in enumerate(v):\n",
        "                items.extend(flatten_dict({f\"{k}[{i}]\": item}, parent_key, sep=sep).items())\n",
        "        else:\n",
        "            items.append((new_key, v))\n",
        "    return dict(items)\n",
        "\n",
        "# Example\n",
        "nested_dict = {\n",
        "    \"road\": {\n",
        "        \"name\": \"Highway 1\",\n",
        "        \"length\": 350,\n",
        "        \"sections\": [\n",
        "            {\n",
        "                \"id\": 1,\n",
        "                \"condition\": {\n",
        "                    \"pavement\": \"good\",\n",
        "                    \"traffic\": \"moderate\"\n",
        "                }\n",
        "            }\n",
        "        ]\n",
        "    }\n",
        "}\n",
        "\n",
        "flattened_dict = flatten_dict(nested_dict)\n",
        "print(flattened_dict)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GYrfRMtgBy9M",
        "outputId": "10947d5c-ab2c-4735-b7fb-ef1a18103065"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'road.name': 'Highway 1', 'road.length': 350, 'road.sections[0].id': 1, 'road.sections[0].condition.pavement': 'good', 'road.sections[0].condition.traffic': 'moderate'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from itertools import permutations\n",
        "\n",
        "def unique_permutations(lst):\n",
        "    # Generate all permutations\n",
        "    all_perms = permutations(lst)\n",
        "    # Use a set to filter out duplicate permutations\n",
        "    unique_perms = set(all_perms)\n",
        "    # Convert each permutation from tuple back to list\n",
        "    return [list(perm) for perm in unique_perms]\n",
        "\n",
        "# Example\n",
        "input_list = [1, 1, 2]\n",
        "output = unique_permutations(input_list)\n",
        "print(output)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "P1WuBgitB-mV",
        "outputId": "e96a3873-7e2d-40e1-fb97-2df9c255395a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1, 2, 1], [2, 1, 1], [1, 1, 2]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "def find_all_dates(text):\n",
        "    # Define the regex patterns for the different date formats\n",
        "    date_patterns = [\n",
        "        r'\\b\\d{2}-\\d{2}-\\d{4}\\b',  # dd-mm-yyyy\n",
        "        r'\\b\\d{2}/\\d{2}/\\d{4}\\b',  # mm/dd/yyyy\n",
        "        r'\\b\\d{4}\\.\\d{2}\\.\\d{2}\\b'  # yyyy.mm.dd\n",
        "    ]\n",
        "\n",
        "    # Combine all patterns into one\n",
        "    combined_pattern = '|'.join(date_patterns)\n",
        "\n",
        "    # Find all matches in the text\n",
        "    matches = re.findall(combined_pattern, text)\n",
        "\n",
        "    return matches\n",
        "\n",
        "# Example\n",
        "text = \"I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23.\"\n",
        "print(find_all_dates(text))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z5V_7A-eCAbm",
        "outputId": "144d09af-e41b-4041-939b-94563c87935c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['23-08-1994', '08/23/1994', '1994.08.23']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import polyline\n",
        "import pandas as pd\n",
        "from math import radians, sin, cos, sqrt, atan2\n",
        "\n",
        "def haversine(lat1, lon1, lat2, lon2):\n",
        "    # Radius of the Earth in meters\n",
        "    R = 6371000\n",
        "    # Convert latitude and longitude from degrees to radians\n",
        "    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])\n",
        "    # Haversine formula\n",
        "    dlat = lat2 - lat1\n",
        "    dlon = lon2 - lon1\n",
        "    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2\n",
        "    c = 2 * atan2(sqrt(a), sqrt(1 - a))\n",
        "    distance = R * c\n",
        "    return distance\n",
        "\n",
        "def decode_polyline_to_df(polyline_str):\n",
        "    # Decode the polyline string into a list of (latitude, longitude) tuples\n",
        "    coordinates = polyline.decode(polyline_str)\n",
        "\n",
        "    # Create a DataFrame from the coordinates\n",
        "    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])\n",
        "\n",
        "    # Calculate distances between successive points\n",
        "    distances = [0]  # First point has a distance of 0\n",
        "    for i in range(1, len(coordinates)):\n",
        "        lat1, lon1 = coordinates[i - 1]\n",
        "        lat2, lon2 = coordinates[i]\n",
        "        distance = haversine(lat1, lon1, lat2, lon2)\n",
        "        distances.append(distance)\n",
        "\n",
        "    # Add the distances to the DataFrame\n",
        "    df['distance'] = distances\n",
        "\n",
        "    return df\n",
        "\n",
        "# Example usage\n",
        "polyline_str = 'u{~vFvyys@fS]'\n",
        "df = decode_polyline_to_df(polyline_str)\n",
        "print(df)\n"
      ],
      "metadata": {
        "id": "BOGbiPdNDn5z",
        "outputId": "46510812-9d5c-4cf6-d780-af34e715d975",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 401
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'polyline'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-11-960cc8a54f98>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mpolyline\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mmath\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mradians\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcos\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msqrt\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0matan2\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mhaversine\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlat1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlon1\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlat2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlon2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'polyline'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install polyline pandas\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HUbHwKL0fma0",
        "outputId": "ded41ba4-dee9-4246-f60c-f5a19d8f821c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting polyline\n",
            "  Downloading polyline-2.0.2-py3-none-any.whl.metadata (6.4 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (2.2.2)\n",
            "Requirement already satisfied: numpy>=1.22.4 in /usr/local/lib/python3.10/dist-packages (from pandas) (1.26.4)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas) (2024.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
            "Downloading polyline-2.0.2-py3-none-any.whl (6.0 kB)\n",
            "Installing collected packages: polyline\n",
            "Successfully installed polyline-2.0.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import polyline\n",
        "import pandas as pd\n",
        "import math\n",
        "\n",
        "def haversine(coord1, coord2):\n",
        "    # Calculate the Haversine distance between two points on the Earth\n",
        "    R = 6371000  # Radius of the Earth in meters\n",
        "    lat1, lon1 = coord1\n",
        "    lat2, lon2 = coord2\n",
        "\n",
        "    # Convert latitude and longitude from degrees to radians\n",
        "    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])\n",
        "\n",
        "    # Haversine formula\n",
        "    dlat = lat2 - lat1\n",
        "    dlon = lon2 - lon1\n",
        "    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2\n",
        "    c = 2 * math.asin(math.sqrt(a))\n",
        "\n",
        "    return R * c  # Return distance in meters\n",
        "\n",
        "def decode_polyline_to_dataframe(polyline_str):\n",
        "    try:\n",
        "        # Decode the polyline string into a list of (latitude, longitude) tuples\n",
        "        coordinates = polyline.decode(polyline_str)\n",
        "        print(f\"Decoded coordinates: {coordinates}\")  # Debugging line to inspect coordinates\n",
        "    except Exception as e:\n",
        "        raise ValueError(f\"Error decoding polyline: {e}\")\n",
        "\n",
        "    # Check if coordinates are empty\n",
        "    if not coordinates:\n",
        "        raise ValueError(\"No coordinates found from the polyline string\")\n",
        "\n",
        "    # Prepare lists for DataFrame\n",
        "    latitudes = []\n",
        "    longitudes = []\n",
        "    distances = [0]  # First distance is 0 since there's no previous point\n",
        "\n",
        "    # Loop through coordinates to fill latitudes, longitudes, and distances\n",
        "    for i in range(len(coordinates)):\n",
        "        lat, lon = coordinates[i]\n",
        "        latitudes.append(lat)\n",
        "        longitudes.append(lon)\n",
        "\n",
        "        if i > 0:  # Calculate distance only for the second point onward\n",
        "            distance = haversine(coordinates[i - 1], coordinates[i])\n",
        "            distances.append(distance)\n",
        "\n",
        "    # Create DataFrame with latitude, longitude, and distance\n",
        "    df = pd.DataFrame({\n",
        "        'latitude': latitudes,\n",
        "        'longitude': longitudes,\n",
        "        'distance': distances\n",
        "    })\n",
        "\n",
        "    return df\n",
        "\n",
        "# Example usage\n",
        "polyline_str = \"u{~vF~q@s@Qd@c@J|@i@u@d@}AiDg@t@j@q@Jc@H|@\"  # Example polyline string\n",
        "\n",
        "try:\n",
        "    df = decode_polyline_to_dataframe(polyline_str)\n",
        "    print(df)\n",
        "except ValueError as ve:\n",
        "    print(ve)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "h4cbYzgxf-T4",
        "outputId": "3a22dc0d-5562-464a-90e7-02b34412e8e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Error decoding polyline: string index out of range\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def rotate_and_transform(matrix):\n",
        "    n = len(matrix)\n",
        "\n",
        "    # Rotate the matrix by 90 degrees clockwise\n",
        "    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]\n",
        "\n",
        "    # Create the final transformed matrix\n",
        "    final_matrix = [[0] * n for _ in range(n)]\n",
        "\n",
        "    for i in range(n):\n",
        "        for j in range(n):\n",
        "            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]\n",
        "            col_sum = sum(rotated_matrix[k][j] for k in range(n)) - rotated_matrix[i][j]\n",
        "            final_matrix[i][j] = row_sum + col_sum\n",
        "\n",
        "    return final_matrix\n",
        "\n",
        "# Example usage\n",
        "matrix = [\n",
        "    [1, 2, 3],\n",
        "    [4, 5, 6],\n",
        "    [7, 8, 9]\n",
        "]\n",
        "\n",
        "result = rotate_and_transform(matrix)\n",
        "for row in result:\n",
        "    print(row)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iQFT84X_gdrN",
        "outputId": "64ecf301-961d-4422-8e24-38b0e701a17a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[22, 19, 16]\n",
            "[23, 20, 17]\n",
            "[24, 21, 18]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(df.columns)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E9eyNnkjk34e",
        "outputId": "b4386d1a-b20b-4684-ace8-04e041291978"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['id_start', 'id_end', 'distance'], dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns = df.columns.str.strip()\n"
      ],
      "metadata": {
        "id": "OXMdpmfDk6xP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.rename(columns={'Start Day': 'startDay', 'Start Time': 'startTime', 'End Day': 'endDay', 'End Time': 'endTime'}, inplace=True)\n"
      ],
      "metadata": {
        "id": "UzXF5dG7k-c_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from datetime import timedelta\n",
        "\n",
        "# Assuming the week starts on a specific date (e.g., Monday, 2024-01-01)\n",
        "def map_weekday_to_date(start_date, weekday_name):\n",
        "    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']\n",
        "    day_offset = weekdays.index(weekday_name)\n",
        "    return start_date + timedelta(days=day_offset)\n",
        "\n",
        "def time_check(df):\n",
        "    # Example: assume the dataset spans from Monday, 2024-01-01\n",
        "    start_of_week = pd.Timestamp('2024-01-01')  # Adjust this start date as needed\n",
        "\n",
        "    # Map the weekday names to actual dates\n",
        "    df['startDate'] = df['startDay'].apply(lambda day: map_weekday_to_date(start_of_week, day))\n",
        "    df['endDate'] = df['endDay'].apply(lambda day: map_weekday_to_date(start_of_week, day))\n",
        "\n",
        "    # Combine dates and times into proper datetime objects\n",
        "    df['startTimestamp'] = pd.to_datetime(df['startDate'].astype(str) + ' ' + df['startTime'])\n",
        "    df['endTimestamp'] = pd.to_datetime(df['endDate'].astype(str) + ' ' + df['endTime'])\n",
        "\n",
        "    # Group the data by the unique (id, id_2) pairs\n",
        "    grouped = df.groupby(['id', 'id_2'])\n",
        "\n",
        "    def check_full_coverage(group):\n",
        "        # Initialize an array to track whether each day and hour has been covered\n",
        "        week_coverage = np.zeros((7, 24), dtype=bool)\n",
        "\n",
        "        # Loop over each row and mark the corresponding hours and days as covered\n",
        "        for _, row in group.iterrows():\n",
        "            start_day = row['startTimestamp'].dayofweek  # Monday = 0, Sunday = 6\n",
        "            end_day = row['endTimestamp'].dayofweek\n",
        "            start_hour = row['startTimestamp'].hour\n",
        "            end_hour = row['endTimestamp'].hour\n",
        "\n",
        "            if start_day == end_day:\n",
        "                # If the range is within the same day, mark the hours within the day\n",
        "                week_coverage[start_day, start_hour:end_hour+1] = True\n",
        "            else:\n",
        "                # If the range spans multiple days, mark the hours accordingly\n",
        "                # Cover the first day (from start_hour to the end of the day)\n",
        "                week_coverage[start_day, start_hour:] = True\n",
        "\n",
        "                # Cover the last day (from midnight to end_hour)\n",
        "                week_coverage[end_day, :end_hour+1] = True\n",
        "\n",
        "                # Mark the full days in between start_day and end_day\n",
        "                if start_day < end_day:\n",
        "                    for day in range(start_day + 1, end_day):\n",
        "                        week_coverage[day, :] = True\n",
        "\n",
        "        # Check if every day of the week has a full 24-hour coverage\n",
        "        return not np.all(week_coverage)\n",
        "\n",
        "    # Apply the check for each (id, id_2) group and return a boolean series\n",
        "    result = grouped.apply(check_full_coverage)\n",
        "\n",
        "    return result\n",
        "\n",
        "# Example usage with a CSV file\n",
        "df = pd.read_csv('/content/dataset-1.csv')\n",
        "result = time_check(df)\n",
        "print(result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "k2A8NfEFqL6s",
        "outputId": "24b78825-39c4-4a9a-fe38-a2e75d324790"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "id       id_2    \n",
            "1014000  -1           True\n",
            "1014002  -1           True\n",
            "1014003  -1           True\n",
            "1030000  -1           True\n",
            "          1030002    False\n",
            "                     ...  \n",
            "1330016   1330006     True\n",
            "          1330008     True\n",
            "          1330010     True\n",
            "          1330012     True\n",
            "          1330014     True\n",
            "Length: 9254, dtype: bool\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-21-1ed4d3155676>:57: DeprecationWarning: DataFrameGroupBy.apply operated on the grouping columns. This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation. Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.\n",
            "  result = grouped.apply(check_full_coverage)\n"
          ]
        }
      ]
    }
  ]
}