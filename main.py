import sys
import streamlit as st # type: ignore
import pandas as pd # type: ignore
import plotly.graph_objects as go # type: ignore
from streamlit.web import cli as stcli # type: ignore


sys.argv = ["streamlit", "run", "top100.py"]

sys.exit(stcli.main())

