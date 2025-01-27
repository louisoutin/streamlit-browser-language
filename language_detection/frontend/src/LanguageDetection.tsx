import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps
} from "streamlit-component-lib"
import React, { useEffect } from "react"

const LanguageDetection: React.FC<ComponentProps> = (props: any) => {

  // Extract the browser language from the navigator object
  const browserLanguage = navigator.language

  useEffect(() => {
    // Set the component height to 0 to avoid extra space
    Streamlit.setFrameHeight(0);
  }, []);

  useEffect(() => {
    // Send the browser language back to Streamlit
    Streamlit.setComponentValue(browserLanguage);
    Streamlit.setComponentReady();
  }, [browserLanguage]);

  // Render nothing (this component is invisible)
  return <></>;
}

export default withStreamlitConnection(LanguageDetection);