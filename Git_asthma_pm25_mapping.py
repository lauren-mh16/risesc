{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1hkY54i7qdO5UCTqxuYbkg7k171Iev_E7",
      "authorship_tag": "ABX9TyPzot26i0vYWxdSO5+Amn2E",
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
        "<a href=\"https://colab.research.google.com/github/lauren-mh16/risesc_public/blob/main/Git_asthma_pm25_mapping.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import folium\n",
        "from streamlit_folium import st_folium\n",
        "import streamlit as st"
      ],
      "metadata": {
        "id": "UhdIugXFX3JN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "## READ FILES -- update!\n",
        "def load_data():\n",
        "  df_merged = pd.read_csv('data/pm25_asthma_clean.csv')\n",
        "  return df_merged"
      ],
      "metadata": {
        "id": "PPKkeXp9X5Vg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Define functions\n",
        "def pm25_2025_color(pm25_2025):\n",
        "    if pm25_2025 < 6:\n",
        "        return 'green'\n",
        "    elif 6 <= pm25_2025 < 9:\n",
        "        return 'orange'\n",
        "    else:\n",
        "        return 'red'\n",
        "\n",
        "def site_type_icon(name):\n",
        "    name_lower = name.lower()\n",
        "    if 'school' in name_lower:\n",
        "        return 'graduation-cap'\n",
        "    elif 'home' in name_lower:\n",
        "        return 'home'\n",
        "    elif 'park' in name_lower or 'playlot' in name_lower:\n",
        "        return 'leaf'\n",
        "    elif 'office' in name_lower:\n",
        "        return 'building'\n",
        "    else:\n",
        "        return 'map-marker'\n",
        "\n",
        "def create_map(df):\n",
        "    center_lat = df['Latitude'].mean()\n",
        "    center_lon = df['Longitude'].mean()\n",
        "    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)\n",
        "\n",
        "    for _, row in df.iterrows():\n",
        "        popup_text = (\n",
        "            f\"<b>{row['Name']}</b><br>\"\n",
        "            f\"PM2.5 (2024): {row['PM25_2024']:.2f} µg/m³<br>\"\n",
        "            f\"PM2.5 (2025): {row['PM25_2025']:.2f} µg/m³<br>\"\n",
        "            f\"Census Tract: {row['Census_Tract']}<br>\"\n",
        "            f\"Asthma Rate: {row['asthma_rate']} per 1000 (Year: {int(row['year'])})<br>\"\n",
        "            f\"Upper CI: {row['Rate Upper Confidence Interval']}\"\n",
        "        )\n",
        "\n",
        "        color = pm25_2025_color(row['PM25_2025'])\n",
        "        icon_type = site_type_icon(row['Name'])\n",
        "\n",
        "        folium.Marker(\n",
        "            location=(row['Latitude'], row['Longitude']),\n",
        "            popup=folium.Popup(popup_text, max_width=300),\n",
        "            icon=folium.Icon(color=color, icon=icon_type, prefix='fa')\n",
        "        ).add_to(m)\n",
        "\n",
        "    legend_html = \"\"\"\n",
        "    <div style=\"position: fixed;\n",
        "         bottom: 50px; left: 50px; width: 280px; height: auto;\n",
        "         border:2px solid grey; z-index:9999; font-size:16px;\n",
        "         background-color: white; padding: 15px;\">\n",
        "    <b>Legend</b><br><br>\n",
        "    <b>PM2.5 (2025) Color:</b><br>\n",
        "    <span style=\"color:green; font-size:18px;\">■</span> Low (<6 µg/m³)<br>\n",
        "    <span style=\"color:orange; font-size:18px;\">■</span> Moderate (6–9 µg/m³)<br>\n",
        "    <span style=\"color:red; font-size:18px;\">■</span> High (>9 µg/m³)<br><br>\n",
        "    <b>Site Type Icons:</b><br>\n",
        "    <span style=\"font-size:18px;\">🎓</span> School<br>\n",
        "    <span style=\"font-size:18px;\">🏠</span> Home<br>\n",
        "    <span style=\"font-size:18px;\">🌳</span> Park / Playlot<br>\n",
        "    <span style=\"font-size:18px;\">🏢</span> Office<br>\n",
        "    <span style=\"font-size:18px;\">📍</span> Other\n",
        "    </div>\n",
        "    \"\"\"\n",
        "    m.get_root().html.add_child(folium.Element(legend_html))\n",
        "    return m\n",
        "\n",
        "def main():\n",
        "    st.title(\"PM2.5 and Asthma Rate Map (2025 Focus)\")\n",
        "\n",
        "    # Show raw data (optional)\n",
        "    with st.expander(\"Show raw data\"):\n",
        "        st.dataframe(df_merged)\n",
        "\n",
        "    # Create and display map\n",
        "    folium_map = create_map(df_merged)\n",
        "    st_folium(folium_map, width=800, height=600)\n",
        "\n",
        "if __name__ == '__main__':\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 384
        },
        "id": "rTQ0EzWUVf7w",
        "outputId": "e15c6f40-2ae7-440d-898e-a5399cc350a6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'streamlit_folium'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-9a0b0f3eb7ba>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mfolium\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mstreamlit_folium\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mst_folium\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'streamlit_folium'",
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
    }
  ]
}