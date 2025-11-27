# Copia esta función dentro de tu AWS Lambda
def predecir_clima_logica(temp, rhum, pres, month, hour, latitude, dew_point):
    if temp <= 3.05:
        if latitude <= 53.63:
            if rhum <= 98.50:
                if pres <= 1018.95:
                    if rhum <= 78.50:
                        if latitude <= 42.48:
                            if temp <= -9.70:
                                if rhum <= 41.50:
                                    if temp <= -16.85:
                                        if dew_point <= -28.60:
                                            return 'Cloudy'
                                        else:  # dew_point > -28.60
                                            if rhum <= 39.50:
                                                return 'Clear'
                                            else:  # rhum > 39.50
                                                return 'Cloudy'
                                    else:  # temp > -16.85
                                        return 'Clear'
                                else:  # rhum > 41.50
                                    if pres <= 1013.45:
                                        if dew_point <= -22.66:
                                            return 'Cloudy'
                                        else:  # dew_point > -22.66
                                            return 'Rain'
                                    else:  # pres > 1013.45
                                        if dew_point <= -20.16:
                                            if pres <= 1017.35:
                                                return 'Cloudy'
                                            else:  # pres > 1017.35
                                                if pres <= 1017.75:
                                                    return 'Clear'
                                                else:  # pres > 1017.75
                                                    return 'Cloudy'
                                        else:  # dew_point > -20.16
                                            if hour <= 18.50:
                                                return 'Clear'
                                            else:  # hour > 18.50
                                                if pres <= 1017.20:
                                                    return 'Clear'
                                                else:  # pres > 1017.20
                                                    return 'Cloudy'
                            else:  # temp > -9.70
                                if pres <= 1017.75:
                                    if pres <= 1002.70:
                                        if pres <= 1002.25:
                                            if dew_point <= -13.46:
                                                return 'Clear'
                                            else:  # dew_point > -13.46
                                                return 'Clear'
                                        else:  # pres > 1002.25
                                            if dew_point <= -10.63:
                                                return 'Clear'
                                            else:  # dew_point > -10.63
                                                return 'Cloudy'
                                    else:  # pres > 1002.70
                                        return 'Clear'
                                else:  # pres > 1017.75
                                    if hour <= 21.50:
                                        if hour <= 9.50:
                                            return 'Clear'
                                        else:  # hour > 9.50
                                            return 'Clear'
                                    else:  # hour > 21.50
                                        if dew_point <= -5.31:
                                            if temp <= 1.35:
                                                return 'Clear'
                                            else:  # temp > 1.35
                                                return 'Clear'
                                        else:  # dew_point > -5.31
                                            if pres <= 1018.35:
                                                if rhum <= 68.50:
                                                    return 'Snow'
                                                else:  # rhum > 68.50
                                                    return 'Clear'
                                            else:  # pres > 1018.35
                                                if pres <= 1018.45:
                                                    return 'Clear'
                                                else:  # pres > 1018.45
                                                    return 'Clear'
                        else:  # latitude > 42.48
                            if pres <= 1012.55:
                                if month <= 11.50:
                                    if latitude <= 50.40:
                                        if pres <= 1006.35:
                                            if pres <= 999.65:
                                                if hour <= 2.50:
                                                    return 'Rain'
                                                else:  # hour > 2.50
                                                    return 'Snow'
                                            else:  # pres > 999.65
                                                if hour <= 0.50:
                                                    return 'Cloudy'
                                                else:  # hour > 0.50
                                                    return 'Cloudy'
                                        else:  # pres > 1006.35
                                            if temp <= 2.45:
                                                if dew_point <= -4.88:
                                                    return 'Snow'
                                                else:  # dew_point > -4.88
                                                    return 'Snow'
                                            else:  # temp > 2.45
                                                if pres <= 1011.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.95
                                                    return 'Clear'
                                    else:  # latitude > 50.40
                                        if month <= 2.50:
                                            if dew_point <= -2.58:
                                                return 'Clear'
                                            else:  # dew_point > -2.58
                                                return 'Clear'
                                        else:  # month > 2.50
                                            if dew_point <= -2.15:
                                                return 'Clear'
                                            else:  # dew_point > -2.15
                                                if dew_point <= -1.28:
                                                    return 'Cloudy'
                                                else:  # dew_point > -1.28
                                                    return 'Clear'
                                else:  # month > 11.50
                                    if pres <= 997.50:
                                        if dew_point <= -7.62:
                                            return 'Snow'
                                        else:  # dew_point > -7.62
                                            return 'Cloudy'
                                    else:  # pres > 997.50
                                        if temp <= -2.30:
                                            if dew_point <= -11.25:
                                                if temp <= -6.20:
                                                    return 'Cloudy'
                                                else:  # temp > -6.20
                                                    return 'Clear'
                                            else:  # dew_point > -11.25
                                                return 'Cloudy'
                                        else:  # temp > -2.30
                                            if pres <= 1008.80:
                                                if pres <= 1004.05:
                                                    return 'Cloudy'
                                                else:  # pres > 1004.05
                                                    return 'Fog'
                                            else:  # pres > 1008.80
                                                if dew_point <= -7.49:
                                                    return 'Cloudy'
                                                else:  # dew_point > -7.49
                                                    return 'Clear'
                            else:  # pres > 1012.55
                                if month <= 7.50:
                                    if latitude <= 50.40:
                                        if hour <= 14.50:
                                            if dew_point <= -13.69:
                                                if dew_point <= -14.88:
                                                    return 'Cloudy'
                                                else:  # dew_point > -14.88
                                                    return 'Cloudy'
                                            else:  # dew_point > -13.69
                                                if rhum <= 63.00:
                                                    return 'Clear'
                                                else:  # rhum > 63.00
                                                    return 'Cloudy'
                                        else:  # hour > 14.50
                                            if pres <= 1012.90:
                                                return 'Clear'
                                            else:  # pres > 1012.90
                                                return 'Cloudy'
                                    else:  # latitude > 50.40
                                        if dew_point <= -0.65:
                                            return 'Clear'
                                        else:  # dew_point > -0.65
                                            if pres <= 1016.15:
                                                return 'Cloudy'
                                            else:  # pres > 1016.15
                                                return 'Clear'
                                else:  # month > 7.50
                                    if month <= 11.50:
                                        if hour <= 8.50:
                                            return 'Clear'
                                        else:  # hour > 8.50
                                            if temp <= -1.00:
                                                return 'Cloudy'
                                            else:  # temp > -1.00
                                                if pres <= 1015.15:
                                                    return 'Clear'
                                                else:  # pres > 1015.15
                                                    return 'Fog'
                                    else:  # month > 11.50
                                        if dew_point <= -1.45:
                                            if pres <= 1016.30:
                                                if pres <= 1013.65:
                                                    return 'Clear'
                                                else:  # pres > 1013.65
                                                    return 'Cloudy'
                                            else:  # pres > 1016.30
                                                if hour <= 16.00:
                                                    return 'Clear'
                                                else:  # hour > 16.00
                                                    return 'Clear'
                                        else:  # dew_point > -1.45
                                            if hour <= 10.00:
                                                return 'Rain'
                                            else:  # hour > 10.00
                                                return 'Cloudy'
                    else:  # rhum > 78.50
                        if latitude <= 50.40:
                            if temp <= -6.50:
                                if temp <= -16.85:
                                    if pres <= 1016.75:
                                        if dew_point <= -18.52:
                                            if pres <= 1014.65:
                                                if pres <= 1013.55:
                                                    return 'Clear'
                                                else:  # pres > 1013.55
                                                    return 'Cloudy'
                                            else:  # pres > 1014.65
                                                return 'Rain'
                                        else:  # dew_point > -18.52
                                            if pres <= 1013.30:
                                                return 'Rain'
                                            else:  # pres > 1013.30
                                                if hour <= 8.50:
                                                    return 'Rain'
                                                else:  # hour > 8.50
                                                    return 'Cloudy'
                                    else:  # pres > 1016.75
                                        return 'Fog'
                                else:  # temp > -16.85
                                    if pres <= 1012.75:
                                        if pres <= 1011.15:
                                            return 'Clear'
                                        else:  # pres > 1011.15
                                            if dew_point <= -18.29:
                                                if hour <= 11.50:
                                                    return 'Rain'
                                                else:  # hour > 11.50
                                                    return 'Cloudy'
                                            else:  # dew_point > -18.29
                                                if rhum <= 90.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 90.50
                                                    return 'Cloudy'
                                    else:  # pres > 1012.75
                                        if hour <= 13.50:
                                            if pres <= 1013.25:
                                                return 'Clear'
                                            else:  # pres > 1013.25
                                                return 'Clear'
                                        else:  # hour > 13.50
                                            if pres <= 1017.35:
                                                if pres <= 1016.20:
                                                    return 'Cloudy'
                                                else:  # pres > 1016.20
                                                    return 'Cloudy'
                                            else:  # pres > 1017.35
                                                return 'Clear'
                            else:  # temp > -6.50
                                if temp <= 2.45:
                                    if rhum <= 92.50:
                                        if month <= 2.50:
                                            if latitude <= 42.48:
                                                if dew_point <= 0.33:
                                                    return 'Clear'
                                                else:  # dew_point > 0.33
                                                    return 'Snow'
                                            else:  # latitude > 42.48
                                                if pres <= 1015.75:
                                                    return 'Snow'
                                                else:  # pres > 1015.75
                                                    return 'Snow'
                                        else:  # month > 2.50
                                            if month <= 11.50:
                                                if pres <= 1015.15:
                                                    return 'Cloudy'
                                                else:  # pres > 1015.15
                                                    return 'Fog'
                                            else:  # month > 11.50
                                                if temp <= -2.95:
                                                    return 'Snow'
                                                else:  # temp > -2.95
                                                    return 'Snow'
                                    else:  # rhum > 92.50
                                        if pres <= 993.20:
                                            if hour <= 7.00:
                                                return 'Cloudy'
                                            else:  # hour > 7.00
                                                return 'Rain'
                                        else:  # pres > 993.20
                                            if dew_point <= 1.99:
                                                if pres <= 993.95:
                                                    return 'Snow'
                                                else:  # pres > 993.95
                                                    return 'Snow'
                                            else:  # dew_point > 1.99
                                                return 'Rain'
                                else:  # temp > 2.45
                                    if pres <= 1018.15:
                                        if pres <= 1012.45:
                                            if hour <= 19.50:
                                                if hour <= 2.50:
                                                    return 'Rain'
                                                else:  # hour > 2.50
                                                    return 'Snow'
                                            else:  # hour > 19.50
                                                if latitude <= 42.48:
                                                    return 'Clear'
                                                else:  # latitude > 42.48
                                                    return 'Rain'
                                        else:  # pres > 1012.45
                                            if dew_point <= 1.66:
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Fog'
                                            else:  # dew_point > 1.66
                                                if temp <= 2.55:
                                                    return 'Fog'
                                                else:  # temp > 2.55
                                                    return 'Snow'
                                    else:  # pres > 1018.15
                                        if dew_point <= 2.30:
                                            if hour <= 12.50:
                                                if hour <= 4.50:
                                                    return 'Rain'
                                                else:  # hour > 4.50
                                                    return 'Fog'
                                            else:  # hour > 12.50
                                                if rhum <= 81.00:
                                                    return 'Rain'
                                                else:  # rhum > 81.00
                                                    return 'Cloudy'
                                        else:  # dew_point > 2.30
                                            if pres <= 1018.70:
                                                return 'Rain'
                                            else:  # pres > 1018.70
                                                return 'Snow'
                        else:  # latitude > 50.40
                            if temp <= 1.35:
                                if month <= 3.50:
                                    if pres <= 1007.45:
                                        if month <= 1.50:
                                            if dew_point <= -0.98:
                                                if temp <= -1.45:
                                                    return 'Clear'
                                                else:  # temp > -1.45
                                                    return 'Cloudy'
                                            else:  # dew_point > -0.98
                                                if pres <= 993.00:
                                                    return 'Clear'
                                                else:  # pres > 993.00
                                                    return 'Snow'
                                        else:  # month > 1.50
                                            if temp <= 0.65:
                                                if dew_point <= -4.63:
                                                    return 'Cloudy'
                                                else:  # dew_point > -4.63
                                                    return 'Snow'
                                            else:  # temp > 0.65
                                                if rhum <= 88.00:
                                                    return 'Cloudy'
                                                else:  # rhum > 88.00
                                                    return 'Snow'
                                    else:  # pres > 1007.45
                                        if rhum <= 92.50:
                                            if month <= 1.50:
                                                if dew_point <= -0.40:
                                                    return 'Clear'
                                                else:  # dew_point > -0.40
                                                    return 'Cloudy'
                                            else:  # month > 1.50
                                                if pres <= 1014.60:
                                                    return 'Cloudy'
                                                else:  # pres > 1014.60
                                                    return 'Clear'
                                        else:  # rhum > 92.50
                                            if hour <= 11.00:
                                                if pres <= 1013.90:
                                                    return 'Cloudy'
                                                else:  # pres > 1013.90
                                                    return 'Cloudy'
                                            else:  # hour > 11.00
                                                if dew_point <= -1.50:
                                                    return 'Cloudy'
                                                else:  # dew_point > -1.50
                                                    return 'Cloudy'
                                else:  # month > 3.50
                                    if rhum <= 95.50:
                                        if pres <= 1006.65:
                                            if dew_point <= -0.77:
                                                if dew_point <= -1.74:
                                                    return 'Cloudy'
                                                else:  # dew_point > -1.74
                                                    return 'Clear'
                                            else:  # dew_point > -0.77
                                                return 'Cloudy'
                                        else:  # pres > 1006.65
                                            if dew_point <= -1.37:
                                                if dew_point <= -3.58:
                                                    return 'Clear'
                                                else:  # dew_point > -3.58
                                                    return 'Clear'
                                            else:  # dew_point > -1.37
                                                if temp <= -0.45:
                                                    return 'Fog'
                                                else:  # temp > -0.45
                                                    return 'Cloudy'
                                    else:  # rhum > 95.50
                                        if pres <= 1016.85:
                                            if dew_point <= 0.78:
                                                if month <= 11.50:
                                                    return 'Fog'
                                                else:  # month > 11.50
                                                    return 'Fog'
                                            else:  # dew_point > 0.78
                                                if hour <= 16.50:
                                                    return 'Snow'
                                                else:  # hour > 16.50
                                                    return 'Cloudy'
                                        else:  # pres > 1016.85
                                            if dew_point <= -0.82:
                                                if month <= 11.50:
                                                    return 'Cloudy'
                                                else:  # month > 11.50
                                                    return 'Clear'
                                            else:  # dew_point > -0.82
                                                if hour <= 9.50:
                                                    return 'Cloudy'
                                                else:  # hour > 9.50
                                                    return 'Snow'
                            else:  # temp > 1.35
                                if pres <= 1000.05:
                                    if month <= 11.50:
                                        if dew_point <= 0.77:
                                            if month <= 2.50:
                                                if pres <= 996.25:
                                                    return 'Cloudy'
                                                else:  # pres > 996.25
                                                    return 'Cloudy'
                                            else:  # month > 2.50
                                                if rhum <= 92.00:
                                                    return 'Clear'
                                                else:  # rhum > 92.00
                                                    return 'Cloudy'
                                        else:  # dew_point > 0.77
                                            if rhum <= 94.50:
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                            else:  # rhum > 94.50
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Rain'
                                    else:  # month > 11.50
                                        if rhum <= 89.50:
                                            if pres <= 973.60:
                                                return 'Clear'
                                            else:  # pres > 973.60
                                                return 'Cloudy'
                                        else:  # rhum > 89.50
                                            if dew_point <= 1.73:
                                                return 'Cloudy'
                                            else:  # dew_point > 1.73
                                                return 'Rain'
                                else:  # pres > 1000.05
                                    if rhum <= 87.50:
                                        if pres <= 1006.70:
                                            if month <= 2.50:
                                                if dew_point <= 0.35:
                                                    return 'Clear'
                                                else:  # dew_point > 0.35
                                                    return 'Rain'
                                            else:  # month > 2.50
                                                if pres <= 1000.60:
                                                    return 'Cloudy'
                                                else:  # pres > 1000.60
                                                    return 'Snow'
                                        else:  # pres > 1006.70
                                            if pres <= 1013.05:
                                                if month <= 2.50:
                                                    return 'Clear'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                            else:  # pres > 1013.05
                                                if hour <= 11.50:
                                                    return 'Clear'
                                                else:  # hour > 11.50
                                                    return 'Cloudy'
                                    else:  # rhum > 87.50
                                        if dew_point <= 2.00:
                                            if rhum <= 92.50:
                                                if hour <= 10.50:
                                                    return 'Clear'
                                                else:  # hour > 10.50
                                                    return 'Cloudy'
                                            else:  # rhum > 92.50
                                                if temp <= 2.05:
                                                    return 'Cloudy'
                                                else:  # temp > 2.05
                                                    return 'Cloudy'
                                        else:  # dew_point > 2.00
                                            if pres <= 1015.30:
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Cloudy'
                                            else:  # pres > 1015.30
                                                if rhum <= 96.00:
                                                    return 'Rain'
                                                else:  # rhum > 96.00
                                                    return 'Fog'
                else:  # pres > 1018.95
                    if latitude <= 50.40:
                        if dew_point <= -10.54:
                            if rhum <= 47.50:
                                if dew_point <= -14.67:
                                    if pres <= 1022.95:
                                        if pres <= 1019.85:
                                            if pres <= 1019.75:
                                                return 'Cloudy'
                                            else:  # pres > 1019.75
                                                return 'Clear'
                                        else:  # pres > 1019.85
                                            return 'Cloudy'
                                    else:  # pres > 1022.95
                                        if temp <= -1.55:
                                            return 'Clear'
                                        else:  # temp > -1.55
                                            return 'Clear'
                                else:  # dew_point > -14.67
                                    if latitude <= 42.48:
                                        if rhum <= 31.50:
                                            return 'Clear'
                                        else:  # rhum > 31.50
                                            return 'Clear'
                                    else:  # latitude > 42.48
                                        if hour <= 18.50:
                                            if dew_point <= -11.27:
                                                if temp <= -3.05:
                                                    return 'Cloudy'
                                                else:  # temp > -3.05
                                                    return 'Clear'
                                            else:  # dew_point > -11.27
                                                if dew_point <= -11.15:
                                                    return 'Cloudy'
                                                else:  # dew_point > -11.15
                                                    return 'Clear'
                                        else:  # hour > 18.50
                                            return 'Cloudy'
                            else:  # rhum > 47.50
                                if dew_point <= -18.04:
                                    if temp <= -16.85:
                                        return 'Fog'
                                    else:  # temp > -16.85
                                        if rhum <= 78.50:
                                            if hour <= 17.50:
                                                return 'Clear'
                                            else:  # hour > 17.50
                                                if rhum <= 68.50:
                                                    return 'Clear'
                                                else:  # rhum > 68.50
                                                    return 'Cloudy'
                                        else:  # rhum > 78.50
                                            if hour <= 16.50:
                                                if pres <= 1021.15:
                                                    return 'Cloudy'
                                                else:  # pres > 1021.15
                                                    return 'Clear'
                                            else:  # hour > 16.50
                                                if rhum <= 82.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 82.50
                                                    return 'Rain'
                                else:  # dew_point > -18.04
                                    if hour <= 2.50:
                                        if rhum <= 79.00:
                                            return 'Cloudy'
                                        else:  # rhum > 79.00
                                            return 'Clear'
                                    else:  # hour > 2.50
                                        if dew_point <= -11.48:
                                            if pres <= 1019.30:
                                                if hour <= 11.50:
                                                    return 'Clear'
                                                else:  # hour > 11.50
                                                    return 'Rain'
                                            else:  # pres > 1019.30
                                                if pres <= 1020.95:
                                                    return 'Fog'
                                                else:  # pres > 1020.95
                                                    return 'Fog'
                                        else:  # dew_point > -11.48
                                            if pres <= 1036.95:
                                                if pres <= 1022.20:
                                                    return 'Clear'
                                                else:  # pres > 1022.20
                                                    return 'Cloudy'
                                            else:  # pres > 1036.95
                                                return 'Fog'
                        else:  # dew_point > -10.54
                            if dew_point <= 1.30:
                                if rhum <= 88.50:
                                    if latitude <= 42.48:
                                        if hour <= 6.50:
                                            if hour <= 1.50:
                                                if rhum <= 37.50:
                                                    return 'Clear'
                                                else:  # rhum > 37.50
                                                    return 'Clear'
                                            else:  # hour > 1.50
                                                return 'Snow'
                                        else:  # hour > 6.50
                                            if pres <= 1028.05:
                                                if dew_point <= -2.77:
                                                    return 'Clear'
                                                else:  # dew_point > -2.77
                                                    return 'Clear'
                                            else:  # pres > 1028.05
                                                if pres <= 1028.60:
                                                    return 'Snow'
                                                else:  # pres > 1028.60
                                                    return 'Clear'
                                    else:  # latitude > 42.48
                                        if temp <= -4.05:
                                            if hour <= 12.50:
                                                if hour <= 2.00:
                                                    return 'Cloudy'
                                                else:  # hour > 2.00
                                                    return 'Snow'
                                            else:  # hour > 12.50
                                                if pres <= 1033.40:
                                                    return 'Cloudy'
                                                else:  # pres > 1033.40
                                                    return 'Cloudy'
                                        else:  # temp > -4.05
                                            if hour <= 16.50:
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Fog'
                                            else:  # hour > 16.50
                                                if hour <= 20.50:
                                                    return 'Snow'
                                                else:  # hour > 20.50
                                                    return 'Cloudy'
                                else:  # rhum > 88.50
                                    if temp <= 1.85:
                                        if pres <= 1026.75:
                                            if pres <= 1019.05:
                                                if latitude <= 42.48:
                                                    return 'Clear'
                                                else:  # latitude > 42.48
                                                    return 'Fog'
                                            else:  # pres > 1019.05
                                                if hour <= 12.50:
                                                    return 'Snow'
                                                else:  # hour > 12.50
                                                    return 'Snow'
                                        else:  # pres > 1026.75
                                            if rhum <= 96.50:
                                                if month <= 4.50:
                                                    return 'Snow'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                            else:  # rhum > 96.50
                                                if month <= 6.50:
                                                    return 'Fog'
                                                else:  # month > 6.50
                                                    return 'Clear'
                                    else:  # temp > 1.85
                                        if hour <= 18.50:
                                            if pres <= 1023.50:
                                                if rhum <= 93.50:
                                                    return 'Fog'
                                                else:  # rhum > 93.50
                                                    return 'Rain'
                                            else:  # pres > 1023.50
                                                if rhum <= 94.50:
                                                    return 'Clear'
                                                else:  # rhum > 94.50
                                                    return 'Fog'
                                        else:  # hour > 18.50
                                            if temp <= 2.35:
                                                if pres <= 1026.35:
                                                    return 'Snow'
                                                else:  # pres > 1026.35
                                                    return 'Cloudy'
                                            else:  # temp > 2.35
                                                return 'Cloudy'
                            else:  # dew_point > 1.30
                                if hour <= 2.50:
                                    if temp <= 2.45:
                                        if month <= 7.00:
                                            if hour <= 1.50:
                                                return 'Snow'
                                            else:  # hour > 1.50
                                                if dew_point <= 1.70:
                                                    return 'Rain'
                                                else:  # dew_point > 1.70
                                                    return 'Snow'
                                        else:  # month > 7.00
                                            if dew_point <= 1.41:
                                                return 'Cloudy'
                                            else:  # dew_point > 1.41
                                                return 'Clear'
                                    else:  # temp > 2.45
                                        if month <= 6.50:
                                            if dew_point <= 1.95:
                                                return 'Cloudy'
                                            else:  # dew_point > 1.95
                                                if pres <= 1024.20:
                                                    return 'Rain'
                                                else:  # pres > 1024.20
                                                    return 'Clear'
                                        else:  # month > 6.50
                                            if month <= 11.50:
                                                return 'Fog'
                                            else:  # month > 11.50
                                                return 'Clear'
                                else:  # hour > 2.50
                                    if pres <= 1022.35:
                                        if month <= 7.00:
                                            if hour <= 22.50:
                                                if latitude <= 42.48:
                                                    return 'Rain'
                                                else:  # latitude > 42.48
                                                    return 'Rain'
                                            else:  # hour > 22.50
                                                if rhum <= 95.50:
                                                    return 'Snow'
                                                else:  # rhum > 95.50
                                                    return 'Rain'
                                        else:  # month > 7.00
                                            if hour <= 15.50:
                                                if rhum <= 96.50:
                                                    return 'Fog'
                                                else:  # rhum > 96.50
                                                    return 'Cloudy'
                                            else:  # hour > 15.50
                                                if pres <= 1020.20:
                                                    return 'Snow'
                                                else:  # pres > 1020.20
                                                    return 'Clear'
                                    else:  # pres > 1022.35
                                        if pres <= 1029.35:
                                            if hour <= 13.50:
                                                if month <= 1.50:
                                                    return 'Fog'
                                                else:  # month > 1.50
                                                    return 'Fog'
                                            else:  # hour > 13.50
                                                if pres <= 1022.70:
                                                    return 'Rain'
                                                else:  # pres > 1022.70
                                                    return 'Fog'
                                        else:  # pres > 1029.35
                                            if dew_point <= 2.10:
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 2.10
                                                if pres <= 1031.15:
                                                    return 'Clear'
                                                else:  # pres > 1031.15
                                                    return 'Fog'
                    else:  # latitude > 50.40
                        if rhum <= 94.50:
                            if pres <= 1020.75:
                                if month <= 1.50:
                                    if dew_point <= 0.56:
                                        if hour <= 7.50:
                                            if temp <= -1.20:
                                                return 'Clear'
                                            else:  # temp > -1.20
                                                return 'Cloudy'
                                        else:  # hour > 7.50
                                            if hour <= 20.50:
                                                if rhum <= 90.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 90.50
                                                    return 'Snow'
                                            else:  # hour > 20.50
                                                if dew_point <= -0.75:
                                                    return 'Clear'
                                                else:  # dew_point > -0.75
                                                    return 'Cloudy'
                                    else:  # dew_point > 0.56
                                        if rhum <= 90.50:
                                            if temp <= 2.95:
                                                return 'Clear'
                                            else:  # temp > 2.95
                                                return 'Cloudy'
                                        else:  # rhum > 90.50
                                            if pres <= 1019.25:
                                                return 'Cloudy'
                                            else:  # pres > 1019.25
                                                if hour <= 21.00:
                                                    return 'Rain'
                                                else:  # hour > 21.00
                                                    return 'Clear'
                                else:  # month > 1.50
                                    if month <= 8.00:
                                        if temp <= 2.85:
                                            return 'Clear'
                                        else:  # temp > 2.85
                                            if pres <= 1020.20:
                                                return 'Clear'
                                            else:  # pres > 1020.20
                                                return 'Cloudy'
                                    else:  # month > 8.00
                                        if hour <= 13.50:
                                            return 'Cloudy'
                                        else:  # hour > 13.50
                                            return 'Clear'
                            else:  # pres > 1020.75
                                if month <= 11.50:
                                    if month <= 3.50:
                                        if pres <= 1034.95:
                                            if pres <= 1026.55:
                                                if temp <= -0.05:
                                                    return 'Clear'
                                                else:  # temp > -0.05
                                                    return 'Clear'
                                            else:  # pres > 1026.55
                                                if dew_point <= -3.19:
                                                    return 'Cloudy'
                                                else:  # dew_point > -3.19
                                                    return 'Cloudy'
                                        else:  # pres > 1034.95
                                            if dew_point <= -1.15:
                                                if temp <= -2.70:
                                                    return 'Cloudy'
                                                else:  # temp > -2.70
                                                    return 'Clear'
                                            else:  # dew_point > -1.15
                                                if hour <= 6.50:
                                                    return 'Clear'
                                                else:  # hour > 6.50
                                                    return 'Clear'
                                    else:  # month > 3.50
                                        if pres <= 1034.45:
                                            if dew_point <= -1.93:
                                                return 'Clear'
                                            else:  # dew_point > -1.93
                                                if rhum <= 85.50:
                                                    return 'Clear'
                                                else:  # rhum > 85.50
                                                    return 'Clear'
                                        else:  # pres > 1034.45
                                            if rhum <= 93.00:
                                                if temp <= 2.20:
                                                    return 'Clear'
                                                else:  # temp > 2.20
                                                    return 'Clear'
                                            else:  # rhum > 93.00
                                                if pres <= 1034.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1034.95
                                                    return 'Clear'
                                else:  # month > 11.50
                                    if pres <= 1030.40:
                                        if dew_point <= -1.12:
                                            if hour <= 20.50:
                                                if hour <= 3.50:
                                                    return 'Clear'
                                                else:  # hour > 3.50
                                                    return 'Cloudy'
                                            else:  # hour > 20.50
                                                if rhum <= 84.50:
                                                    return 'Clear'
                                                else:  # rhum > 84.50
                                                    return 'Clear'
                                        else:  # dew_point > -1.12
                                            if rhum <= 85.50:
                                                if temp <= 2.15:
                                                    return 'Clear'
                                                else:  # temp > 2.15
                                                    return 'Cloudy'
                                            else:  # rhum > 85.50
                                                if temp <= 1.95:
                                                    return 'Cloudy'
                                                else:  # temp > 1.95
                                                    return 'Cloudy'
                                    else:  # pres > 1030.40
                                        if pres <= 1030.55:
                                            return 'Clear'
                                        else:  # pres > 1030.55
                                            return 'Clear'
                        else:  # rhum > 94.50
                            if hour <= 3.50:
                                if pres <= 1027.95:
                                    if temp <= -2.85:
                                        if hour <= 2.00:
                                            return 'Fog'
                                        else:  # hour > 2.00
                                            return 'Clear'
                                    else:  # temp > -2.85
                                        if temp <= -1.00:
                                            return 'Clear'
                                        else:  # temp > -1.00
                                            if rhum <= 95.50:
                                                if temp <= 1.90:
                                                    return 'Cloudy'
                                                else:  # temp > 1.90
                                                    return 'Clear'
                                            else:  # rhum > 95.50
                                                return 'Cloudy'
                                else:  # pres > 1027.95
                                    if dew_point <= -1.07:
                                        if pres <= 1033.05:
                                            return 'Clear'
                                        else:  # pres > 1033.05
                                            return 'Fog'
                                    else:  # dew_point > -1.07
                                        if dew_point <= 2.03:
                                            if hour <= 1.50:
                                                if rhum <= 97.50:
                                                    return 'Clear'
                                                else:  # rhum > 97.50
                                                    return 'Cloudy'
                                            else:  # hour > 1.50
                                                if pres <= 1034.00:
                                                    return 'Cloudy'
                                                else:  # pres > 1034.00
                                                    return 'Fog'
                                        else:  # dew_point > 2.03
                                            if rhum <= 96.50:
                                                return 'Clear'
                                            else:  # rhum > 96.50
                                                if pres <= 1033.10:
                                                    return 'Fog'
                                                else:  # pres > 1033.10
                                                    return 'Fog'
                            else:  # hour > 3.50
                                if pres <= 1024.45:
                                    if hour <= 9.50:
                                        if dew_point <= 2.20:
                                            if month <= 6.50:
                                                if dew_point <= 0.48:
                                                    return 'Clear'
                                                else:  # dew_point > 0.48
                                                    return 'Cloudy'
                                            else:  # month > 6.50
                                                if hour <= 4.50:
                                                    return 'Clear'
                                                else:  # hour > 4.50
                                                    return 'Cloudy'
                                        else:  # dew_point > 2.20
                                            if temp <= 2.75:
                                                return 'Fog'
                                            else:  # temp > 2.75
                                                return 'Clear'
                                    else:  # hour > 9.50
                                        if pres <= 1020.55:
                                            if dew_point <= 1.20:
                                                return 'Cloudy'
                                            else:  # dew_point > 1.20
                                                if hour <= 22.50:
                                                    return 'Rain'
                                                else:  # hour > 22.50
                                                    return 'Cloudy'
                                        else:  # pres > 1020.55
                                            if month <= 6.00:
                                                if dew_point <= 1.18:
                                                    return 'Snow'
                                                else:  # dew_point > 1.18
                                                    return 'Rain'
                                            else:  # month > 6.00
                                                if pres <= 1021.30:
                                                    return 'Clear'
                                                else:  # pres > 1021.30
                                                    return 'Cloudy'
                                else:  # pres > 1024.45
                                    if hour <= 6.50:
                                        if rhum <= 95.50:
                                            if dew_point <= 2.23:
                                                return 'Clear'
                                            else:  # dew_point > 2.23
                                                if month <= 2.50:
                                                    return 'Cloudy'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                        else:  # rhum > 95.50
                                            if pres <= 1035.85:
                                                if pres <= 1031.80:
                                                    return 'Cloudy'
                                                else:  # pres > 1031.80
                                                    return 'Clear'
                                            else:  # pres > 1035.85
                                                if dew_point <= 1.92:
                                                    return 'Cloudy'
                                                else:  # dew_point > 1.92
                                                    return 'Clear'
                                    else:  # hour > 6.50
                                        if pres <= 1040.80:
                                            if pres <= 1033.75:
                                                if pres <= 1032.40:
                                                    return 'Cloudy'
                                                else:  # pres > 1032.40
                                                    return 'Fog'
                                            else:  # pres > 1033.75
                                                if hour <= 9.50:
                                                    return 'Cloudy'
                                                else:  # hour > 9.50
                                                    return 'Clear'
                                        else:  # pres > 1040.80
                                            if pres <= 1043.40:
                                                if hour <= 16.00:
                                                    return 'Fog'
                                                else:  # hour > 16.00
                                                    return 'Clear'
                                            else:  # pres > 1043.40
                                                if pres <= 1045.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1045.95
                                                    return 'Clear'
            else:  # rhum > 98.50
                if pres <= 998.45:
                    if dew_point <= 1.43:
                        if pres <= 990.95:
                            if month <= 7.50:
                                return 'Rain'
                            else:  # month > 7.50
                                if hour <= 7.50:
                                    return 'Cloudy'
                                else:  # hour > 7.50
                                    return 'Cloudy'
                        else:  # pres > 990.95
                            if hour <= 7.50:
                                return 'Rain'
                            else:  # hour > 7.50
                                if hour <= 9.50:
                                    if pres <= 996.85:
                                        return 'Rain'
                                    else:  # pres > 996.85
                                        return 'Snow'
                                else:  # hour > 9.50
                                    if pres <= 993.95:
                                        if temp <= 0.60:
                                            return 'Rain'
                                        else:  # temp > 0.60
                                            return 'Snow'
                                    else:  # pres > 993.95
                                        return 'Snow'
                    else:  # dew_point > 1.43
                        if pres <= 996.85:
                            return 'Rain'
                        else:  # pres > 996.85
                            if temp <= 2.80:
                                return 'Clear'
                            else:  # temp > 2.80
                                return 'Clear'
                else:  # pres > 998.45
                    if hour <= 11.50:
                        if latitude <= 50.40:
                            if pres <= 1025.60:
                                if dew_point <= -1.02:
                                    if dew_point <= -11.10:
                                        if pres <= 1018.90:
                                            if pres <= 1016.75:
                                                if hour <= 8.50:
                                                    return 'Cloudy'
                                                else:  # hour > 8.50
                                                    return 'Cloudy'
                                            else:  # pres > 1016.75
                                                return 'Clear'
                                        else:  # pres > 1018.90
                                            return 'Fog'
                                    else:  # dew_point > -11.10
                                        return 'Snow'
                                else:  # dew_point > -1.02
                                    if pres <= 1007.90:
                                        return 'Rain'
                                    else:  # pres > 1007.90
                                        if pres <= 1021.45:
                                            if temp <= 2.30:
                                                if hour <= 8.50:
                                                    return 'Cloudy'
                                                else:  # hour > 8.50
                                                    return 'Rain'
                                            else:  # temp > 2.30
                                                if hour <= 9.50:
                                                    return 'Cloudy'
                                                else:  # hour > 9.50
                                                    return 'Clear'
                                        else:  # pres > 1021.45
                                            return 'Clear'
                            else:  # pres > 1025.60
                                if month <= 11.50:
                                    return 'Fog'
                                else:  # month > 11.50
                                    if pres <= 1028.00:
                                        return 'Clear'
                                    else:  # pres > 1028.00
                                        return 'Clear'
                        else:  # latitude > 50.40
                            if temp <= 2.75:
                                if rhum <= 99.50:
                                    if pres <= 1008.30:
                                        if pres <= 1000.85:
                                            if temp <= 1.00:
                                                return 'Fog'
                                            else:  # temp > 1.00
                                                if temp <= 1.50:
                                                    return 'Cloudy'
                                                else:  # temp > 1.50
                                                    return 'Fog'
                                        else:  # pres > 1000.85
                                            if dew_point <= 0.86:
                                                if pres <= 1003.85:
                                                    return 'Cloudy'
                                                else:  # pres > 1003.85
                                                    return 'Clear'
                                            else:  # dew_point > 0.86
                                                if dew_point <= 1.21:
                                                    return 'Rain'
                                                else:  # dew_point > 1.21
                                                    return 'Rain'
                                    else:  # pres > 1008.30
                                        if pres <= 1011.20:
                                            if hour <= 0.50:
                                                return 'Clear'
                                            else:  # hour > 0.50
                                                if pres <= 1009.65:
                                                    return 'Fog'
                                                else:  # pres > 1009.65
                                                    return 'Fog'
                                        else:  # pres > 1011.20
                                            if month <= 11.50:
                                                if pres <= 1020.30:
                                                    return 'Fog'
                                                else:  # pres > 1020.30
                                                    return 'Fog'
                                            else:  # month > 11.50
                                                if hour <= 4.50:
                                                    return 'Clear'
                                                else:  # hour > 4.50
                                                    return 'Cloudy'
                                else:  # rhum > 99.50
                                    if dew_point <= 1.25:
                                        if temp <= -3.80:
                                            if dew_point <= -4.05:
                                                return 'Cloudy'
                                            else:  # dew_point > -4.05
                                                return 'Clear'
                                        else:  # temp > -3.80
                                            if dew_point <= 0.55:
                                                if pres <= 1021.00:
                                                    return 'Fog'
                                                else:  # pres > 1021.00
                                                    return 'Fog'
                                            else:  # dew_point > 0.55
                                                if pres <= 1002.55:
                                                    return 'Fog'
                                                else:  # pres > 1002.55
                                                    return 'Fog'
                                    else:  # dew_point > 1.25
                                        if pres <= 1020.25:
                                            if pres <= 1016.25:
                                                return 'Fog'
                                            else:  # pres > 1016.25
                                                if month <= 6.00:
                                                    return 'Rain'
                                                else:  # month > 6.00
                                                    return 'Cloudy'
                                        else:  # pres > 1020.25
                                            if hour <= 10.00:
                                                if month <= 11.50:
                                                    return 'Fog'
                                                else:  # month > 11.50
                                                    return 'Clear'
                                            else:  # hour > 10.00
                                                return 'Cloudy'
                            else:  # temp > 2.75
                                if pres <= 1034.50:
                                    if pres <= 1003.95:
                                        return 'Clear'
                                    else:  # pres > 1003.95
                                        if pres <= 1020.20:
                                            if dew_point <= 2.78:
                                                return 'Cloudy'
                                            else:  # dew_point > 2.78
                                                return 'Rain'
                                        else:  # pres > 1020.20
                                            if temp <= 2.95:
                                                return 'Cloudy'
                                            else:  # temp > 2.95
                                                return 'Clear'
                                else:  # pres > 1034.50
                                    return 'Fog'
                    else:  # hour > 11.50
                        if month <= 7.00:
                            if pres <= 1021.65:
                                if dew_point <= 1.93:
                                    if temp <= -0.50:
                                        if hour <= 21.50:
                                            return 'Cloudy'
                                        else:  # hour > 21.50
                                            return 'Fog'
                                    else:  # temp > -0.50
                                        if hour <= 20.50:
                                            if pres <= 1020.35:
                                                if pres <= 1019.45:
                                                    return 'Snow'
                                                else:  # pres > 1019.45
                                                    return 'Snow'
                                            else:  # pres > 1020.35
                                                if pres <= 1020.65:
                                                    return 'Cloudy'
                                                else:  # pres > 1020.65
                                                    return 'Cloudy'
                                        else:  # hour > 20.50
                                            if pres <= 1017.15:
                                                return 'Rain'
                                            else:  # pres > 1017.15
                                                return 'Rain'
                                else:  # dew_point > 1.93
                                    if latitude <= 42.48:
                                        return 'Clear'
                                    else:  # latitude > 42.48
                                        if hour <= 13.50:
                                            if dew_point <= 2.21:
                                                return 'Cloudy'
                                            else:  # dew_point > 2.21
                                                if temp <= 2.65:
                                                    return 'Rain'
                                                else:  # temp > 2.65
                                                    return 'Cloudy'
                                        else:  # hour > 13.50
                                            return 'Rain'
                            else:  # pres > 1021.65
                                if pres <= 1030.20:
                                    if temp <= 2.90:
                                        if pres <= 1027.70:
                                            if pres <= 1027.55:
                                                if hour <= 12.50:
                                                    return 'Cloudy'
                                                else:  # hour > 12.50
                                                    return 'Fog'
                                            else:  # pres > 1027.55
                                                return 'Cloudy'
                                        else:  # pres > 1027.70
                                            return 'Fog'
                                    else:  # temp > 2.90
                                        return 'Rain'
                                else:  # pres > 1030.20
                                    if temp <= 0.75:
                                        return 'Cloudy'
                                    else:  # temp > 0.75
                                        return 'Cloudy'
                        else:  # month > 7.00
                            if dew_point <= 1.83:
                                if dew_point <= -3.07:
                                    return 'Clear'
                                else:  # dew_point > -3.07
                                    if hour <= 14.50:
                                        if temp <= 1.35:
                                            if pres <= 1007.90:
                                                return 'Cloudy'
                                            else:  # pres > 1007.90
                                                if temp <= -1.25:
                                                    return 'Fog'
                                                else:  # temp > -1.25
                                                    return 'Fog'
                                        else:  # temp > 1.35
                                            if pres <= 1015.30:
                                                return 'Rain'
                                            else:  # pres > 1015.30
                                                if temp <= 1.85:
                                                    return 'Clear'
                                                else:  # temp > 1.85
                                                    return 'Cloudy'
                                    else:  # hour > 14.50
                                        if pres <= 1009.80:
                                            if hour <= 19.50:
                                                return 'Cloudy'
                                            else:  # hour > 19.50
                                                if pres <= 1009.00:
                                                    return 'Fog'
                                                else:  # pres > 1009.00
                                                    return 'Clear'
                                        else:  # pres > 1009.80
                                            if dew_point <= 1.71:
                                                if temp <= -2.05:
                                                    return 'Fog'
                                                else:  # temp > -2.05
                                                    return 'Fog'
                                            else:  # dew_point > 1.71
                                                if latitude <= 50.40:
                                                    return 'Fog'
                                                else:  # latitude > 50.40
                                                    return 'Cloudy'
                            else:  # dew_point > 1.83
                                if pres <= 1016.15:
                                    if pres <= 1014.25:
                                        if temp <= 1.95:
                                            return 'Cloudy'
                                        else:  # temp > 1.95
                                            return 'Rain'
                                    else:  # pres > 1014.25
                                        return 'Cloudy'
                                else:  # pres > 1016.15
                                    if rhum <= 99.50:
                                        if temp <= 2.05:
                                            return 'Clear'
                                        else:  # temp > 2.05
                                            if hour <= 22.50:
                                                if pres <= 1024.35:
                                                    return 'Fog'
                                                else:  # pres > 1024.35
                                                    return 'Fog'
                                            else:  # hour > 22.50
                                                return 'Clear'
                                    else:  # rhum > 99.50
                                        if hour <= 13.50:
                                            return 'Clear'
                                        else:  # hour > 13.50
                                            return 'Clear'
        else:  # latitude > 53.63
            if rhum <= 69.50:
                if pres <= 1010.95:
                    if pres <= 999.75:
                        if dew_point <= -10.74:
                            if pres <= 981.80:
                                if dew_point <= -11.08:
                                    return 'Snow'
                                else:  # dew_point > -11.08
                                    return 'Cloudy'
                            else:  # pres > 981.80
                                if pres <= 998.65:
                                    if pres <= 989.30:
                                        if rhum <= 45.00:
                                            if temp <= -3.50:
                                                return 'Clear'
                                            else:  # temp > -3.50
                                                return 'Cloudy'
                                        else:  # rhum > 45.00
                                            if hour <= 2.50:
                                                return 'Clear'
                                            else:  # hour > 2.50
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Cloudy'
                                    else:  # pres > 989.30
                                        if dew_point <= -17.44:
                                            return 'Cloudy'
                                        else:  # dew_point > -17.44
                                            if dew_point <= -11.81:
                                                if dew_point <= -15.92:
                                                    return 'Clear'
                                                else:  # dew_point > -15.92
                                                    return 'Clear'
                                            else:  # dew_point > -11.81
                                                if temp <= -1.10:
                                                    return 'Clear'
                                                else:  # temp > -1.10
                                                    return 'Clear'
                                else:  # pres > 998.65
                                    if rhum <= 50.50:
                                        if temp <= -3.30:
                                            return 'Snow'
                                        else:  # temp > -3.30
                                            if hour <= 20.50:
                                                return 'Clear'
                                            else:  # hour > 20.50
                                                return 'Cloudy'
                                    else:  # rhum > 50.50
                                        if temp <= -4.25:
                                            return 'Clear'
                                        else:  # temp > -4.25
                                            if hour <= 14.00:
                                                if hour <= 12.00:
                                                    return 'Clear'
                                                else:  # hour > 12.00
                                                    return 'Cloudy'
                                            else:  # hour > 14.00
                                                return 'Clear'
                        else:  # dew_point > -10.74
                            if pres <= 960.50:
                                if rhum <= 64.50:
                                    if hour <= 10.50:
                                        if dew_point <= -3.69:
                                            return 'Clear'
                                        else:  # dew_point > -3.69
                                            return 'Cloudy'
                                    else:  # hour > 10.50
                                        return 'Cloudy'
                                else:  # rhum > 64.50
                                    return 'Clear'
                            else:  # pres > 960.50
                                if temp <= -0.95:
                                    if pres <= 988.15:
                                        if temp <= -3.40:
                                            if pres <= 987.45:
                                                if hour <= 18.00:
                                                    return 'Cloudy'
                                                else:  # hour > 18.00
                                                    return 'Clear'
                                            else:  # pres > 987.45
                                                return 'Clear'
                                        else:  # temp > -3.40
                                            if month <= 7.00:
                                                if dew_point <= -10.12:
                                                    return 'Clear'
                                                else:  # dew_point > -10.12
                                                    return 'Snow'
                                            else:  # month > 7.00
                                                return 'Clear'
                                    else:  # pres > 988.15
                                        if latitude <= 59.95:
                                            if pres <= 991.80:
                                                return 'Cloudy'
                                            else:  # pres > 991.80
                                                if temp <= -1.05:
                                                    return 'Snow'
                                                else:  # temp > -1.05
                                                    return 'Clear'
                                        else:  # latitude > 59.95
                                            if dew_point <= -7.13:
                                                if hour <= 10.50:
                                                    return 'Snow'
                                                else:  # hour > 10.50
                                                    return 'Snow'
                                            else:  # dew_point > -7.13
                                                if hour <= 20.50:
                                                    return 'Snow'
                                                else:  # hour > 20.50
                                                    return 'Clear'
                                else:  # temp > -0.95
                                    if month <= 2.50:
                                        if pres <= 964.60:
                                            if dew_point <= -6.85:
                                                if hour <= 6.00:
                                                    return 'Snow'
                                                else:  # hour > 6.00
                                                    return 'Cloudy'
                                            else:  # dew_point > -6.85
                                                if rhum <= 64.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 64.50
                                                    return 'Snow'
                                        else:  # pres > 964.60
                                            if pres <= 999.05:
                                                if pres <= 993.85:
                                                    return 'Snow'
                                                else:  # pres > 993.85
                                                    return 'Snow'
                                            else:  # pres > 999.05
                                                if hour <= 14.50:
                                                    return 'Cloudy'
                                                else:  # hour > 14.50
                                                    return 'Clear'
                                    else:  # month > 2.50
                                        if dew_point <= -2.92:
                                            if month <= 11.50:
                                                if month <= 4.50:
                                                    return 'Snow'
                                                else:  # month > 4.50
                                                    return 'Snow'
                                            else:  # month > 11.50
                                                if pres <= 987.50:
                                                    return 'Snow'
                                                else:  # pres > 987.50
                                                    return 'Snow'
                                        else:  # dew_point > -2.92
                                            if pres <= 994.25:
                                                if dew_point <= -2.37:
                                                    return 'Cloudy'
                                                else:  # dew_point > -2.37
                                                    return 'Rain'
                                            else:  # pres > 994.25
                                                return 'Clear'
                    else:  # pres > 999.75
                        if month <= 4.50:
                            if dew_point <= -5.06:
                                if latitude <= 59.95:
                                    if month <= 3.50:
                                        if temp <= -2.70:
                                            if hour <= 14.50:
                                                if hour <= 5.50:
                                                    return 'Clear'
                                                else:  # hour > 5.50
                                                    return 'Snow'
                                            else:  # hour > 14.50
                                                if month <= 1.50:
                                                    return 'Snow'
                                                else:  # month > 1.50
                                                    return 'Cloudy'
                                        else:  # temp > -2.70
                                            if pres <= 1004.50:
                                                if dew_point <= -8.20:
                                                    return 'Clear'
                                                else:  # dew_point > -8.20
                                                    return 'Snow'
                                            else:  # pres > 1004.50
                                                if pres <= 1010.65:
                                                    return 'Cloudy'
                                                else:  # pres > 1010.65
                                                    return 'Snow'
                                    else:  # month > 3.50
                                        if temp <= -1.15:
                                            return 'Clear'
                                        else:  # temp > -1.15
                                            if pres <= 1006.40:
                                                if pres <= 1004.00:
                                                    return 'Cloudy'
                                                else:  # pres > 1004.00
                                                    return 'Clear'
                                            else:  # pres > 1006.40
                                                if temp <= 1.25:
                                                    return 'Cloudy'
                                                else:  # temp > 1.25
                                                    return 'Cloudy'
                                else:  # latitude > 59.95
                                    if temp <= -4.45:
                                        if dew_point <= -12.04:
                                            return 'Clear'
                                        else:  # dew_point > -12.04
                                            if pres <= 1003.50:
                                                if dew_point <= -10.47:
                                                    return 'Cloudy'
                                                else:  # dew_point > -10.47
                                                    return 'Clear'
                                            else:  # pres > 1003.50
                                                if rhum <= 59.50:
                                                    return 'Clear'
                                                else:  # rhum > 59.50
                                                    return 'Clear'
                                    else:  # temp > -4.45
                                        if month <= 3.50:
                                            if month <= 1.50:
                                                if hour <= 4.50:
                                                    return 'Cloudy'
                                                else:  # hour > 4.50
                                                    return 'Snow'
                                            else:  # month > 1.50
                                                if hour <= 3.50:
                                                    return 'Snow'
                                                else:  # hour > 3.50
                                                    return 'Clear'
                                        else:  # month > 3.50
                                            if pres <= 1007.50:
                                                if dew_point <= -12.97:
                                                    return 'Cloudy'
                                                else:  # dew_point > -12.97
                                                    return 'Snow'
                                            else:  # pres > 1007.50
                                                if hour <= 10.50:
                                                    return 'Snow'
                                                else:  # hour > 10.50
                                                    return 'Clear'
                            else:  # dew_point > -5.06
                                if latitude <= 59.95:
                                    if month <= 2.50:
                                        if dew_point <= -4.95:
                                            if hour <= 11.50:
                                                return 'Clear'
                                            else:  # hour > 11.50
                                                return 'Cloudy'
                                        else:  # dew_point > -4.95
                                            if rhum <= 59.50:
                                                if pres <= 1001.55:
                                                    return 'Cloudy'
                                                else:  # pres > 1001.55
                                                    return 'Clear'
                                            else:  # rhum > 59.50
                                                if temp <= 0.40:
                                                    return 'Cloudy'
                                                else:  # temp > 0.40
                                                    return 'Cloudy'
                                    else:  # month > 2.50
                                        if hour <= 12.50:
                                            if hour <= 4.50:
                                                if temp <= 2.25:
                                                    return 'Cloudy'
                                                else:  # temp > 2.25
                                                    return 'Clear'
                                            else:  # hour > 4.50
                                                return 'Cloudy'
                                        else:  # hour > 12.50
                                            if month <= 3.50:
                                                if dew_point <= -3.71:
                                                    return 'Snow'
                                                else:  # dew_point > -3.71
                                                    return 'Cloudy'
                                            else:  # month > 3.50
                                                if temp <= 1.15:
                                                    return 'Cloudy'
                                                else:  # temp > 1.15
                                                    return 'Clear'
                                else:  # latitude > 59.95
                                    if temp <= 0.35:
                                        if hour <= 21.50:
                                            if hour <= 17.00:
                                                if hour <= 4.50:
                                                    return 'Cloudy'
                                                else:  # hour > 4.50
                                                    return 'Cloudy'
                                            else:  # hour > 17.00
                                                return 'Clear'
                                        else:  # hour > 21.50
                                            if pres <= 1008.50:
                                                return 'Cloudy'
                                            else:  # pres > 1008.50
                                                if pres <= 1009.50:
                                                    return 'Snow'
                                                else:  # pres > 1009.50
                                                    return 'Clear'
                                    else:  # temp > 0.35
                                        if hour <= 22.50:
                                            if dew_point <= -3.59:
                                                if month <= 1.50:
                                                    return 'Snow'
                                                else:  # month > 1.50
                                                    return 'Snow'
                                            else:  # dew_point > -3.59
                                                if month <= 1.50:
                                                    return 'Snow'
                                                else:  # month > 1.50
                                                    return 'Cloudy'
                                        else:  # hour > 22.50
                                            if month <= 1.50:
                                                if rhum <= 66.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 66.50
                                                    return 'Clear'
                                            else:  # month > 1.50
                                                return 'Clear'
                        else:  # month > 4.50
                            if pres <= 1008.05:
                                if dew_point <= -15.04:
                                    if pres <= 1003.35:
                                        return 'Snow'
                                    else:  # pres > 1003.35
                                        if rhum <= 67.50:
                                            return 'Clear'
                                        else:  # rhum > 67.50
                                            return 'Cloudy'
                                else:  # dew_point > -15.04
                                    if pres <= 1007.65:
                                        if month <= 11.50:
                                            if rhum <= 64.50:
                                                if dew_point <= -6.26:
                                                    return 'Clear'
                                                else:  # dew_point > -6.26
                                                    return 'Snow'
                                            else:  # rhum > 64.50
                                                if rhum <= 68.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 68.50
                                                    return 'Clear'
                                        else:  # month > 11.50
                                            if hour <= 9.50:
                                                if temp <= -0.60:
                                                    return 'Snow'
                                                else:  # temp > -0.60
                                                    return 'Cloudy'
                                            else:  # hour > 9.50
                                                if temp <= -7.80:
                                                    return 'Clear'
                                                else:  # temp > -7.80
                                                    return 'Cloudy'
                                    else:  # pres > 1007.65
                                        if hour <= 12.50:
                                            if dew_point <= -4.51:
                                                if rhum <= 50.00:
                                                    return 'Cloudy'
                                                else:  # rhum > 50.00
                                                    return 'Clear'
                                            else:  # dew_point > -4.51
                                                if temp <= 2.50:
                                                    return 'Cloudy'
                                                else:  # temp > 2.50
                                                    return 'Cloudy'
                                        else:  # hour > 12.50
                                            if temp <= 1.50:
                                                if rhum <= 54.50:
                                                    return 'Clear'
                                                else:  # rhum > 54.50
                                                    return 'Snow'
                                            else:  # temp > 1.50
                                                if dew_point <= -4.51:
                                                    return 'Clear'
                                                else:  # dew_point > -4.51
                                                    return 'Cloudy'
                            else:  # pres > 1008.05
                                if dew_point <= -4.27:
                                    if latitude <= 59.95:
                                        if hour <= 20.00:
                                            return 'Cloudy'
                                        else:  # hour > 20.00
                                            return 'Clear'
                                    else:  # latitude > 59.95
                                        if hour <= 12.50:
                                            return 'Clear'
                                        else:  # hour > 12.50
                                            if hour <= 19.50:
                                                if dew_point <= -9.12:
                                                    return 'Cloudy'
                                                else:  # dew_point > -9.12
                                                    return 'Clear'
                                            else:  # hour > 19.50
                                                if rhum <= 46.00:
                                                    return 'Clear'
                                                else:  # rhum > 46.00
                                                    return 'Clear'
                                else:  # dew_point > -4.27
                                    if month <= 10.50:
                                        if hour <= 4.50:
                                            if dew_point <= -3.64:
                                                return 'Cloudy'
                                            else:  # dew_point > -3.64
                                                return 'Clear'
                                        else:  # hour > 4.50
                                            if hour <= 11.00:
                                                return 'Clear'
                                            else:  # hour > 11.00
                                                if temp <= 2.85:
                                                    return 'Cloudy'
                                                else:  # temp > 2.85
                                                    return 'Clear'
                                    else:  # month > 10.50
                                        if dew_point <= -4.08:
                                            if pres <= 1009.50:
                                                if hour <= 12.00:
                                                    return 'Clear'
                                                else:  # hour > 12.00
                                                    return 'Cloudy'
                                            else:  # pres > 1009.50
                                                return 'Cloudy'
                                        else:  # dew_point > -4.08
                                            if pres <= 1010.45:
                                                if hour <= 4.50:
                                                    return 'Cloudy'
                                                else:  # hour > 4.50
                                                    return 'Cloudy'
                                            else:  # pres > 1010.45
                                                return 'Clear'
                else:  # pres > 1010.95
                    if rhum <= 59.50:
                        if month <= 1.50:
                            if hour <= 2.50:
                                if pres <= 1013.50:
                                    if pres <= 1012.50:
                                        if temp <= -3.00:
                                            return 'Clear'
                                        else:  # temp > -3.00
                                            return 'Cloudy'
                                    else:  # pres > 1012.50
                                        if hour <= 0.50:
                                            return 'Clear'
                                        else:  # hour > 0.50
                                            if dew_point <= -12.51:
                                                return 'Snow'
                                            else:  # dew_point > -12.51
                                                if hour <= 1.50:
                                                    return 'Snow'
                                                else:  # hour > 1.50
                                                    return 'Cloudy'
                                else:  # pres > 1013.50
                                    if rhum <= 56.00:
                                        return 'Cloudy'
                                    else:  # rhum > 56.00
                                        if temp <= -0.50:
                                            return 'Clear'
                                        else:  # temp > -0.50
                                            return 'Cloudy'
                            else:  # hour > 2.50
                                if rhum <= 51.50:
                                    if temp <= -3.65:
                                        return 'Clear'
                                    else:  # temp > -3.65
                                        if hour <= 21.50:
                                            if hour <= 5.50:
                                                if temp <= -1.30:
                                                    return 'Cloudy'
                                                else:  # temp > -1.30
                                                    return 'Clear'
                                            else:  # hour > 5.50
                                                return 'Cloudy'
                                        else:  # hour > 21.50
                                            if pres <= 1014.50:
                                                if pres <= 1013.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1013.50
                                                    return 'Cloudy'
                                            else:  # pres > 1014.50
                                                return 'Clear'
                                else:  # rhum > 51.50
                                    if pres <= 1017.20:
                                        if rhum <= 54.50:
                                            if pres <= 1013.20:
                                                if hour <= 22.50:
                                                    return 'Cloudy'
                                                else:  # hour > 22.50
                                                    return 'Clear'
                                            else:  # pres > 1013.20
                                                return 'Clear'
                                        else:  # rhum > 54.50
                                            if pres <= 1014.95:
                                                return 'Clear'
                                            else:  # pres > 1014.95
                                                if rhum <= 58.50:
                                                    return 'Clear'
                                                else:  # rhum > 58.50
                                                    return 'Cloudy'
                                    else:  # pres > 1017.20
                                        if hour <= 14.50:
                                            if pres <= 1022.60:
                                                if dew_point <= -10.61:
                                                    return 'Clear'
                                                else:  # dew_point > -10.61
                                                    return 'Cloudy'
                                            else:  # pres > 1022.60
                                                return 'Cloudy'
                                        else:  # hour > 14.50
                                            if pres <= 1029.05:
                                                return 'Cloudy'
                                            else:  # pres > 1029.05
                                                if dew_point <= -16.64:
                                                    return 'Cloudy'
                                                else:  # dew_point > -16.64
                                                    return 'Snow'
                        else:  # month > 1.50
                            if rhum <= 55.50:
                                if pres <= 1013.95:
                                    if hour <= 1.50:
                                        if pres <= 1011.20:
                                            if temp <= -1.30:
                                                return 'Snow'
                                            else:  # temp > -1.30
                                                return 'Clear'
                                        else:  # pres > 1011.20
                                            if pres <= 1011.70:
                                                return 'Cloudy'
                                            else:  # pres > 1011.70
                                                if rhum <= 52.50:
                                                    return 'Clear'
                                                else:  # rhum > 52.50
                                                    return 'Cloudy'
                                    else:  # hour > 1.50
                                        if dew_point <= -16.14:
                                            return 'Clear'
                                        else:  # dew_point > -16.14
                                            if hour <= 15.50:
                                                if month <= 3.50:
                                                    return 'Cloudy'
                                                else:  # month > 3.50
                                                    return 'Clear'
                                            else:  # hour > 15.50
                                                if dew_point <= -12.55:
                                                    return 'Cloudy'
                                                else:  # dew_point > -12.55
                                                    return 'Clear'
                                else:  # pres > 1013.95
                                    if dew_point <= -8.95:
                                        if latitude <= 59.95:
                                            if pres <= 1023.30:
                                                if hour <= 11.50:
                                                    return 'Clear'
                                                else:  # hour > 11.50
                                                    return 'Cloudy'
                                            else:  # pres > 1023.30
                                                if temp <= -2.25:
                                                    return 'Clear'
                                                else:  # temp > -2.25
                                                    return 'Clear'
                                        else:  # latitude > 59.95
                                            if pres <= 1021.85:
                                                if rhum <= 53.50:
                                                    return 'Clear'
                                                else:  # rhum > 53.50
                                                    return 'Clear'
                                            else:  # pres > 1021.85
                                                if pres <= 1022.10:
                                                    return 'Snow'
                                                else:  # pres > 1022.10
                                                    return 'Clear'
                                    else:  # dew_point > -8.95
                                        if month <= 3.50:
                                            if pres <= 1020.60:
                                                if rhum <= 47.50:
                                                    return 'Clear'
                                                else:  # rhum > 47.50
                                                    return 'Cloudy'
                                            else:  # pres > 1020.60
                                                if temp <= 0.05:
                                                    return 'Snow'
                                                else:  # temp > 0.05
                                                    return 'Clear'
                                        else:  # month > 3.50
                                            if month <= 4.50:
                                                if hour <= 12.50:
                                                    return 'Clear'
                                                else:  # hour > 12.50
                                                    return 'Clear'
                                            else:  # month > 4.50
                                                if latitude <= 59.95:
                                                    return 'Clear'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                            else:  # rhum > 55.50
                                if pres <= 1026.15:
                                    if hour <= 6.50:
                                        if temp <= 2.40:
                                            if temp <= -5.30:
                                                if temp <= -10.70:
                                                    return 'Cloudy'
                                                else:  # temp > -10.70
                                                    return 'Clear'
                                            else:  # temp > -5.30
                                                if pres <= 1016.45:
                                                    return 'Clear'
                                                else:  # pres > 1016.45
                                                    return 'Clear'
                                        else:  # temp > 2.40
                                            if rhum <= 56.50:
                                                return 'Cloudy'
                                            else:  # rhum > 56.50
                                                return 'Cloudy'
                                    else:  # hour > 6.50
                                        if month <= 3.50:
                                            if temp <= -6.85:
                                                if rhum <= 56.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 56.50
                                                    return 'Clear'
                                            else:  # temp > -6.85
                                                if dew_point <= -11.98:
                                                    return 'Snow'
                                                else:  # dew_point > -11.98
                                                    return 'Snow'
                                        else:  # month > 3.50
                                            if temp <= -0.85:
                                                if rhum <= 56.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 56.50
                                                    return 'Clear'
                                            else:  # temp > -0.85
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Snow'
                                else:  # pres > 1026.15
                                    if temp <= -5.55:
                                        if dew_point <= -14.59:
                                            if pres <= 1043.80:
                                                return 'Clear'
                                            else:  # pres > 1043.80
                                                if pres <= 1046.65:
                                                    return 'Cloudy'
                                                else:  # pres > 1046.65
                                                    return 'Clear'
                                        else:  # dew_point > -14.59
                                            if pres <= 1038.20:
                                                if hour <= 14.50:
                                                    return 'Cloudy'
                                                else:  # hour > 14.50
                                                    return 'Cloudy'
                                            else:  # pres > 1038.20
                                                if month <= 8.00:
                                                    return 'Clear'
                                                else:  # month > 8.00
                                                    return 'Cloudy'
                                    else:  # temp > -5.55
                                        if hour <= 8.50:
                                            if month <= 8.00:
                                                if hour <= 0.50:
                                                    return 'Clear'
                                                else:  # hour > 0.50
                                                    return 'Clear'
                                            else:  # month > 8.00
                                                if pres <= 1032.15:
                                                    return 'Cloudy'
                                                else:  # pres > 1032.15
                                                    return 'Clear'
                                        else:  # hour > 8.50
                                            if temp <= 0.75:
                                                return 'Clear'
                                            else:  # temp > 0.75
                                                if hour <= 12.50:
                                                    return 'Clear'
                                                else:  # hour > 12.50
                                                    return 'Clear'
                    else:  # rhum > 59.50
                        if month <= 2.50:
                            if temp <= -8.05:
                                if pres <= 1039.40:
                                    if latitude <= 59.95:
                                        if hour <= 11.50:
                                            if temp <= -11.85:
                                                if rhum <= 63.50:
                                                    return 'Clear'
                                                else:  # rhum > 63.50
                                                    return 'Snow'
                                            else:  # temp > -11.85
                                                if temp <= -8.30:
                                                    return 'Cloudy'
                                                else:  # temp > -8.30
                                                    return 'Clear'
                                        else:  # hour > 11.50
                                            if dew_point <= -20.59:
                                                return 'Clear'
                                            else:  # dew_point > -20.59
                                                if pres <= 1026.25:
                                                    return 'Snow'
                                                else:  # pres > 1026.25
                                                    return 'Snow'
                                    else:  # latitude > 59.95
                                        return 'Clear'
                                else:  # pres > 1039.40
                                    if temp <= -18.10:
                                        return 'Clear'
                                    else:  # temp > -18.10
                                        if month <= 1.50:
                                            return 'Cloudy'
                                        else:  # month > 1.50
                                            return 'Cloudy'
                            else:  # temp > -8.05
                                if temp <= 1.95:
                                    if temp <= -1.95:
                                        if dew_point <= -10.34:
                                            if latitude <= 59.95:
                                                if hour <= 15.50:
                                                    return 'Cloudy'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                            else:  # latitude > 59.95
                                                if dew_point <= -10.62:
                                                    return 'Clear'
                                                else:  # dew_point > -10.62
                                                    return 'Cloudy'
                                        else:  # dew_point > -10.34
                                            if pres <= 1024.15:
                                                if pres <= 1015.85:
                                                    return 'Clear'
                                                else:  # pres > 1015.85
                                                    return 'Snow'
                                            else:  # pres > 1024.15
                                                if hour <= 16.00:
                                                    return 'Cloudy'
                                                else:  # hour > 16.00
                                                    return 'Clear'
                                    else:  # temp > -1.95
                                        if hour <= 14.50:
                                            if hour <= 8.50:
                                                if temp <= 0.80:
                                                    return 'Cloudy'
                                                else:  # temp > 0.80
                                                    return 'Clear'
                                            else:  # hour > 8.50
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Cloudy'
                                        else:  # hour > 14.50
                                            if temp <= 0.35:
                                                if pres <= 1016.15:
                                                    return 'Cloudy'
                                                else:  # pres > 1016.15
                                                    return 'Cloudy'
                                            else:  # temp > 0.35
                                                if dew_point <= -5.15:
                                                    return 'Snow'
                                                else:  # dew_point > -5.15
                                                    return 'Cloudy'
                                else:  # temp > 1.95
                                    if hour <= 4.50:
                                        if dew_point <= -3.48:
                                            return 'Clear'
                                        else:  # dew_point > -3.48
                                            if hour <= 1.50:
                                                return 'Clear'
                                            else:  # hour > 1.50
                                                return 'Cloudy'
                                    else:  # hour > 4.50
                                        if latitude <= 59.95:
                                            if dew_point <= -4.27:
                                                return 'Clear'
                                            else:  # dew_point > -4.27
                                                return 'Cloudy'
                                        else:  # latitude > 59.95
                                            if pres <= 1011.80:
                                                return 'Cloudy'
                                            else:  # pres > 1011.80
                                                if hour <= 18.50:
                                                    return 'Snow'
                                                else:  # hour > 18.50
                                                    return 'Clear'
                        else:  # month > 2.50
                            if pres <= 1021.05:
                                if dew_point <= -11.90:
                                    if latitude <= 59.95:
                                        if dew_point <= -12.30:
                                            if temp <= -12.05:
                                                if hour <= 16.50:
                                                    return 'Cloudy'
                                                else:  # hour > 16.50
                                                    return 'Clear'
                                            else:  # temp > -12.05
                                                return 'Cloudy'
                                        else:  # dew_point > -12.30
                                            if pres <= 1014.35:
                                                return 'Clear'
                                            else:  # pres > 1014.35
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Clear'
                                    else:  # latitude > 59.95
                                        if hour <= 14.50:
                                            return 'Clear'
                                        else:  # hour > 14.50
                                            if hour <= 16.50:
                                                if pres <= 1015.60:
                                                    return 'Cloudy'
                                                else:  # pres > 1015.60
                                                    return 'Clear'
                                            else:  # hour > 16.50
                                                return 'Clear'
                                else:  # dew_point > -11.90
                                    if pres <= 1011.15:
                                        if hour <= 6.50:
                                            return 'Clear'
                                        else:  # hour > 6.50
                                            if pres <= 1011.05:
                                                if rhum <= 61.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 61.50
                                                    return 'Clear'
                                            else:  # pres > 1011.05
                                                return 'Cloudy'
                                    else:  # pres > 1011.15
                                        if month <= 4.50:
                                            if temp <= -2.55:
                                                if pres <= 1012.40:
                                                    return 'Cloudy'
                                                else:  # pres > 1012.40
                                                    return 'Snow'
                                            else:  # temp > -2.55
                                                if dew_point <= -5.02:
                                                    return 'Cloudy'
                                                else:  # dew_point > -5.02
                                                    return 'Snow'
                                        else:  # month > 4.50
                                            if month <= 10.50:
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                            else:  # month > 10.50
                                                if dew_point <= -6.38:
                                                    return 'Clear'
                                                else:  # dew_point > -6.38
                                                    return 'Snow'
                            else:  # pres > 1021.05
                                if dew_point <= -8.04:
                                    if pres <= 1022.95:
                                        if latitude <= 59.95:
                                            if hour <= 15.50:
                                                if pres <= 1021.15:
                                                    return 'Clear'
                                                else:  # pres > 1021.15
                                                    return 'Cloudy'
                                            else:  # hour > 15.50
                                                return 'Clear'
                                        else:  # latitude > 59.95
                                            if hour <= 17.50:
                                                if rhum <= 68.50:
                                                    return 'Clear'
                                                else:  # rhum > 68.50
                                                    return 'Cloudy'
                                            else:  # hour > 17.50
                                                if dew_point <= -9.14:
                                                    return 'Cloudy'
                                                else:  # dew_point > -9.14
                                                    return 'Clear'
                                    else:  # pres > 1022.95
                                        if pres <= 1048.15:
                                            if dew_point <= -13.15:
                                                if dew_point <= -13.78:
                                                    return 'Clear'
                                                else:  # dew_point > -13.78
                                                    return 'Cloudy'
                                            else:  # dew_point > -13.15
                                                if pres <= 1024.30:
                                                    return 'Clear'
                                                else:  # pres > 1024.30
                                                    return 'Clear'
                                        else:  # pres > 1048.15
                                            return 'Cloudy'
                                else:  # dew_point > -8.04
                                    if hour <= 20.50:
                                        if dew_point <= -3.78:
                                            if month <= 3.50:
                                                if pres <= 1023.15:
                                                    return 'Snow'
                                                else:  # pres > 1023.15
                                                    return 'Cloudy'
                                            else:  # month > 3.50
                                                if pres <= 1036.90:
                                                    return 'Clear'
                                                else:  # pres > 1036.90
                                                    return 'Cloudy'
                                        else:  # dew_point > -3.78
                                            if pres <= 1026.10:
                                                if pres <= 1023.20:
                                                    return 'Cloudy'
                                                else:  # pres > 1023.20
                                                    return 'Clear'
                                            else:  # pres > 1026.10
                                                return 'Cloudy'
                                    else:  # hour > 20.50
                                        if month <= 10.50:
                                            if temp <= 2.80:
                                                if latitude <= 59.95:
                                                    return 'Clear'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                            else:  # temp > 2.80
                                                if month <= 4.50:
                                                    return 'Cloudy'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                        else:  # month > 10.50
                                            if temp <= 0.15:
                                                if rhum <= 68.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 68.50
                                                    return 'Clear'
                                            else:  # temp > 0.15
                                                return 'Snow'
            else:  # rhum > 69.50
                if dew_point <= 1.04:
                    if pres <= 1021.65:
                        if temp <= 1.15:
                            if rhum <= 79.50:
                                if pres <= 1019.05:
                                    if latitude <= 59.95:
                                        if pres <= 1006.75:
                                            if temp <= 0.85:
                                                if pres <= 999.55:
                                                    return 'Snow'
                                                else:  # pres > 999.55
                                                    return 'Snow'
                                            else:  # temp > 0.85
                                                if dew_point <= -2.71:
                                                    return 'Cloudy'
                                                else:  # dew_point > -2.71
                                                    return 'Snow'
                                        else:  # pres > 1006.75
                                            if dew_point <= -11.48:
                                                if month <= 1.50:
                                                    return 'Snow'
                                                else:  # month > 1.50
                                                    return 'Snow'
                                            else:  # dew_point > -11.48
                                                if pres <= 1013.15:
                                                    return 'Snow'
                                                else:  # pres > 1013.15
                                                    return 'Snow'
                                    else:  # latitude > 59.95
                                        if dew_point <= -5.89:
                                            if dew_point <= -9.29:
                                                if pres <= 1007.30:
                                                    return 'Clear'
                                                else:  # pres > 1007.30
                                                    return 'Clear'
                                            else:  # dew_point > -9.29
                                                if hour <= 11.50:
                                                    return 'Snow'
                                                else:  # hour > 11.50
                                                    return 'Snow'
                                        else:  # dew_point > -5.89
                                            if month <= 4.50:
                                                if pres <= 963.05:
                                                    return 'Cloudy'
                                                else:  # pres > 963.05
                                                    return 'Snow'
                                            else:  # month > 4.50
                                                if pres <= 1013.80:
                                                    return 'Snow'
                                                else:  # pres > 1013.80
                                                    return 'Snow'
                                else:  # pres > 1019.05
                                    if temp <= -5.45:
                                        if month <= 1.50:
                                            if pres <= 1020.75:
                                                if temp <= -19.35:
                                                    return 'Clear'
                                                else:  # temp > -19.35
                                                    return 'Cloudy'
                                            else:  # pres > 1020.75
                                                if temp <= -8.50:
                                                    return 'Clear'
                                                else:  # temp > -8.50
                                                    return 'Cloudy'
                                        else:  # month > 1.50
                                            if hour <= 8.50:
                                                if temp <= -14.35:
                                                    return 'Cloudy'
                                                else:  # temp > -14.35
                                                    return 'Clear'
                                            else:  # hour > 8.50
                                                if rhum <= 71.00:
                                                    return 'Cloudy'
                                                else:  # rhum > 71.00
                                                    return 'Snow'
                                    else:  # temp > -5.45
                                        if dew_point <= -3.12:
                                            if latitude <= 59.95:
                                                if month <= 10.50:
                                                    return 'Cloudy'
                                                else:  # month > 10.50
                                                    return 'Cloudy'
                                            else:  # latitude > 59.95
                                                if pres <= 1021.05:
                                                    return 'Cloudy'
                                                else:  # pres > 1021.05
                                                    return 'Snow'
                                        else:  # dew_point > -3.12
                                            if dew_point <= -2.98:
                                                return 'Snow'
                                            else:  # dew_point > -2.98
                                                if dew_point <= -2.55:
                                                    return 'Cloudy'
                                                else:  # dew_point > -2.55
                                                    return 'Clear'
                            else:  # rhum > 79.50
                                if pres <= 1015.55:
                                    if temp <= 0.05:
                                        if latitude <= 59.95:
                                            if rhum <= 86.50:
                                                if pres <= 1008.35:
                                                    return 'Snow'
                                                else:  # pres > 1008.35
                                                    return 'Snow'
                                            else:  # rhum > 86.50
                                                if dew_point <= -0.24:
                                                    return 'Snow'
                                                else:  # dew_point > -0.24
                                                    return 'Rain'
                                        else:  # latitude > 59.95
                                            if temp <= -6.90:
                                                if pres <= 993.50:
                                                    return 'Snow'
                                                else:  # pres > 993.50
                                                    return 'Clear'
                                            else:  # temp > -6.90
                                                if month <= 6.50:
                                                    return 'Snow'
                                                else:  # month > 6.50
                                                    return 'Snow'
                                    else:  # temp > 0.05
                                        if hour <= 6.50:
                                            if pres <= 1014.95:
                                                if dew_point <= 0.49:
                                                    return 'Snow'
                                                else:  # dew_point > 0.49
                                                    return 'Snow'
                                            else:  # pres > 1014.95
                                                if temp <= 0.50:
                                                    return 'Cloudy'
                                                else:  # temp > 0.50
                                                    return 'Cloudy'
                                        else:  # hour > 6.50
                                            if month <= 6.50:
                                                if pres <= 1015.45:
                                                    return 'Snow'
                                                else:  # pres > 1015.45
                                                    return 'Cloudy'
                                            else:  # month > 6.50
                                                if pres <= 1014.75:
                                                    return 'Snow'
                                                else:  # pres > 1014.75
                                                    return 'Cloudy'
                                else:  # pres > 1015.55
                                    if temp <= -1.65:
                                        if temp <= -21.35:
                                            return 'Clear'
                                        else:  # temp > -21.35
                                            if temp <= -10.85:
                                                if pres <= 1021.25:
                                                    return 'Snow'
                                                else:  # pres > 1021.25
                                                    return 'Clear'
                                            else:  # temp > -10.85
                                                if dew_point <= -12.51:
                                                    return 'Cloudy'
                                                else:  # dew_point > -12.51
                                                    return 'Snow'
                                    else:  # temp > -1.65
                                        if month <= 2.50:
                                            if dew_point <= -3.83:
                                                return 'Cloudy'
                                            else:  # dew_point > -3.83
                                                if pres <= 1021.45:
                                                    return 'Snow'
                                                else:  # pres > 1021.45
                                                    return 'Cloudy'
                                        else:  # month > 2.50
                                            if dew_point <= -2.24:
                                                if pres <= 1019.95:
                                                    return 'Snow'
                                                else:  # pres > 1019.95
                                                    return 'Cloudy'
                                            else:  # dew_point > -2.24
                                                if dew_point <= 0.46:
                                                    return 'Snow'
                                                else:  # dew_point > 0.46
                                                    return 'Rain'
                        else:  # temp > 1.15
                            if dew_point <= 0.05:
                                if pres <= 1005.45:
                                    if temp <= 2.25:
                                        if month <= 3.50:
                                            if dew_point <= -3.24:
                                                if pres <= 986.50:
                                                    return 'Clear'
                                                else:  # pres > 986.50
                                                    return 'Cloudy'
                                            else:  # dew_point > -3.24
                                                if pres <= 983.30:
                                                    return 'Snow'
                                                else:  # pres > 983.30
                                                    return 'Snow'
                                        else:  # month > 3.50
                                            if month <= 10.50:
                                                if hour <= 5.50:
                                                    return 'Cloudy'
                                                else:  # hour > 5.50
                                                    return 'Snow'
                                            else:  # month > 10.50
                                                if temp <= 2.15:
                                                    return 'Snow'
                                                else:  # temp > 2.15
                                                    return 'Cloudy'
                                    else:  # temp > 2.25
                                        if hour <= 0.50:
                                            if pres <= 1004.40:
                                                if temp <= 2.75:
                                                    return 'Rain'
                                                else:  # temp > 2.75
                                                    return 'Rain'
                                            else:  # pres > 1004.40
                                                return 'Cloudy'
                                        else:  # hour > 0.50
                                            if pres <= 996.05:
                                                if dew_point <= -2.04:
                                                    return 'Cloudy'
                                                else:  # dew_point > -2.04
                                                    return 'Snow'
                                            else:  # pres > 996.05
                                                if hour <= 6.50:
                                                    return 'Cloudy'
                                                else:  # hour > 6.50
                                                    return 'Snow'
                                else:  # pres > 1005.45
                                    if month <= 10.50:
                                        if hour <= 9.50:
                                            if pres <= 1013.05:
                                                if dew_point <= -1.94:
                                                    return 'Clear'
                                                else:  # dew_point > -1.94
                                                    return 'Snow'
                                            else:  # pres > 1013.05
                                                if month <= 2.50:
                                                    return 'Snow'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                        else:  # hour > 9.50
                                            if latitude <= 59.95:
                                                if hour <= 19.50:
                                                    return 'Snow'
                                                else:  # hour > 19.50
                                                    return 'Cloudy'
                                            else:  # latitude > 59.95
                                                if temp <= 1.35:
                                                    return 'Cloudy'
                                                else:  # temp > 1.35
                                                    return 'Snow'
                                    else:  # month > 10.50
                                        if temp <= 1.25:
                                            if hour <= 4.50:
                                                if rhum <= 90.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 90.50
                                                    return 'Rain'
                                            else:  # hour > 4.50
                                                if pres <= 1014.90:
                                                    return 'Snow'
                                                else:  # pres > 1014.90
                                                    return 'Cloudy'
                                        else:  # temp > 1.25
                                            if rhum <= 75.50:
                                                if pres <= 1012.85:
                                                    return 'Cloudy'
                                                else:  # pres > 1012.85
                                                    return 'Snow'
                                            else:  # rhum > 75.50
                                                if rhum <= 84.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 84.50
                                                    return 'Cloudy'
                            else:  # dew_point > 0.05
                                if temp <= 2.05:
                                    if pres <= 985.90:
                                        if hour <= 6.50:
                                            if hour <= 3.50:
                                                if hour <= 2.50:
                                                    return 'Rain'
                                                else:  # hour > 2.50
                                                    return 'Snow'
                                            else:  # hour > 3.50
                                                if pres <= 976.90:
                                                    return 'Rain'
                                                else:  # pres > 976.90
                                                    return 'Rain'
                                        else:  # hour > 6.50
                                            if hour <= 20.50:
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Snow'
                                            else:  # hour > 20.50
                                                if hour <= 21.50:
                                                    return 'Fog'
                                                else:  # hour > 21.50
                                                    return 'Rain'
                                    else:  # pres > 985.90
                                        if pres <= 1008.40:
                                            if month <= 11.50:
                                                if month <= 1.50:
                                                    return 'Snow'
                                                else:  # month > 1.50
                                                    return 'Snow'
                                            else:  # month > 11.50
                                                if hour <= 6.50:
                                                    return 'Snow'
                                                else:  # hour > 6.50
                                                    return 'Snow'
                                        else:  # pres > 1008.40
                                            if dew_point <= 0.11:
                                                if hour <= 19.50:
                                                    return 'Snow'
                                                else:  # hour > 19.50
                                                    return 'Fog'
                                            else:  # dew_point > 0.11
                                                if dew_point <= 0.19:
                                                    return 'Cloudy'
                                                else:  # dew_point > 0.19
                                                    return 'Snow'
                                else:  # temp > 2.05
                                    if pres <= 972.90:
                                        if pres <= 958.70:
                                            if hour <= 14.50:
                                                if pres <= 948.70:
                                                    return 'Rain'
                                                else:  # pres > 948.70
                                                    return 'Cloudy'
                                            else:  # hour > 14.50
                                                return 'Snow'
                                        else:  # pres > 958.70
                                            if dew_point <= 0.92:
                                                if temp <= 2.20:
                                                    return 'Cloudy'
                                                else:  # temp > 2.20
                                                    return 'Rain'
                                            else:  # dew_point > 0.92
                                                return 'Cloudy'
                                    else:  # pres > 972.90
                                        if pres <= 1017.15:
                                            if hour <= 0.50:
                                                if month <= 4.50:
                                                    return 'Rain'
                                                else:  # month > 4.50
                                                    return 'Cloudy'
                                            else:  # hour > 0.50
                                                if hour <= 19.50:
                                                    return 'Snow'
                                                else:  # hour > 19.50
                                                    return 'Snow'
                                        else:  # pres > 1017.15
                                            if dew_point <= 0.13:
                                                if dew_point <= 0.11:
                                                    return 'Rain'
                                                else:  # dew_point > 0.11
                                                    return 'Snow'
                                            else:  # dew_point > 0.13
                                                if hour <= 19.50:
                                                    return 'Cloudy'
                                                else:  # hour > 19.50
                                                    return 'Cloudy'
                    else:  # pres > 1021.65
                        if pres <= 1036.65:
                            if temp <= -7.05:
                                if dew_point <= -19.61:
                                    if dew_point <= -20.15:
                                        if dew_point <= -20.50:
                                            return 'Clear'
                                        else:  # dew_point > -20.50
                                            if dew_point <= -20.45:
                                                if hour <= 4.00:
                                                    return 'Clear'
                                                else:  # hour > 4.00
                                                    return 'Cloudy'
                                            else:  # dew_point > -20.45
                                                return 'Clear'
                                    else:  # dew_point > -20.15
                                        if hour <= 7.50:
                                            if temp <= -17.50:
                                                if rhum <= 86.50:
                                                    return 'Clear'
                                                else:  # rhum > 86.50
                                                    return 'Cloudy'
                                            else:  # temp > -17.50
                                                if temp <= -16.70:
                                                    return 'Cloudy'
                                                else:  # temp > -16.70
                                                    return 'Clear'
                                        else:  # hour > 7.50
                                            return 'Clear'
                                else:  # dew_point > -19.61
                                    if latitude <= 59.95:
                                        if pres <= 1024.45:
                                            if rhum <= 75.50:
                                                if hour <= 7.50:
                                                    return 'Cloudy'
                                                else:  # hour > 7.50
                                                    return 'Clear'
                                            else:  # rhum > 75.50
                                                if temp <= -11.85:
                                                    return 'Snow'
                                                else:  # temp > -11.85
                                                    return 'Snow'
                                        else:  # pres > 1024.45
                                            if rhum <= 88.50:
                                                if dew_point <= -18.05:
                                                    return 'Clear'
                                                else:  # dew_point > -18.05
                                                    return 'Snow'
                                            else:  # rhum > 88.50
                                                if pres <= 1026.55:
                                                    return 'Snow'
                                                else:  # pres > 1026.55
                                                    return 'Cloudy'
                                    else:  # latitude > 59.95
                                        if pres <= 1024.60:
                                            return 'Clear'
                                        else:  # pres > 1024.60
                                            if pres <= 1026.20:
                                                if hour <= 9.00:
                                                    return 'Clear'
                                                else:  # hour > 9.00
                                                    return 'Cloudy'
                                            else:  # pres > 1026.20
                                                return 'Clear'
                            else:  # temp > -7.05
                                if rhum <= 85.50:
                                    if latitude <= 59.95:
                                        if month <= 10.50:
                                            if temp <= -0.85:
                                                if dew_point <= -7.53:
                                                    return 'Cloudy'
                                                else:  # dew_point > -7.53
                                                    return 'Snow'
                                            else:  # temp > -0.85
                                                if month <= 2.50:
                                                    return 'Cloudy'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                        else:  # month > 10.50
                                            if dew_point <= -9.47:
                                                if pres <= 1025.65:
                                                    return 'Cloudy'
                                                else:  # pres > 1025.65
                                                    return 'Clear'
                                            else:  # dew_point > -9.47
                                                if dew_point <= -0.42:
                                                    return 'Snow'
                                                else:  # dew_point > -0.42
                                                    return 'Cloudy'
                                    else:  # latitude > 59.95
                                        if dew_point <= -7.32:
                                            if pres <= 1026.50:
                                                if month <= 2.00:
                                                    return 'Cloudy'
                                                else:  # month > 2.00
                                                    return 'Clear'
                                            else:  # pres > 1026.50
                                                if rhum <= 70.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 70.50
                                                    return 'Clear'
                                        else:  # dew_point > -7.32
                                            if dew_point <= -1.00:
                                                if month <= 11.50:
                                                    return 'Snow'
                                                else:  # month > 11.50
                                                    return 'Clear'
                                            else:  # dew_point > -1.00
                                                if pres <= 1022.05:
                                                    return 'Snow'
                                                else:  # pres > 1022.05
                                                    return 'Cloudy'
                                else:  # rhum > 85.50
                                    if pres <= 1030.15:
                                        if dew_point <= 0.65:
                                            if pres <= 1025.05:
                                                if temp <= -4.35:
                                                    return 'Snow'
                                                else:  # temp > -4.35
                                                    return 'Snow'
                                            else:  # pres > 1025.05
                                                if temp <= 1.85:
                                                    return 'Snow'
                                                else:  # temp > 1.85
                                                    return 'Rain'
                                        else:  # dew_point > 0.65
                                            if month <= 3.50:
                                                if hour <= 13.00:
                                                    return 'Fog'
                                                else:  # hour > 13.00
                                                    return 'Cloudy'
                                            else:  # month > 3.50
                                                if hour <= 13.00:
                                                    return 'Cloudy'
                                                else:  # hour > 13.00
                                                    return 'Cloudy'
                                    else:  # pres > 1030.15
                                        if dew_point <= -1.46:
                                            if temp <= -1.35:
                                                if temp <= -4.85:
                                                    return 'Cloudy'
                                                else:  # temp > -4.85
                                                    return 'Cloudy'
                                            else:  # temp > -1.35
                                                if rhum <= 86.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 86.50
                                                    return 'Snow'
                                        else:  # dew_point > -1.46
                                            if pres <= 1033.35:
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                            else:  # pres > 1033.35
                                                if pres <= 1035.45:
                                                    return 'Clear'
                                                else:  # pres > 1035.45
                                                    return 'Cloudy'
                        else:  # pres > 1036.65
                            if latitude <= 59.95:
                                if pres <= 1042.15:
                                    if temp <= -4.25:
                                        if dew_point <= -6.09:
                                            if month <= 1.50:
                                                if pres <= 1039.55:
                                                    return 'Cloudy'
                                                else:  # pres > 1039.55
                                                    return 'Snow'
                                            else:  # month > 1.50
                                                if rhum <= 75.50:
                                                    return 'Clear'
                                                else:  # rhum > 75.50
                                                    return 'Cloudy'
                                        else:  # dew_point > -6.09
                                            if hour <= 9.50:
                                                if hour <= 5.50:
                                                    return 'Cloudy'
                                                else:  # hour > 5.50
                                                    return 'Snow'
                                            else:  # hour > 9.50
                                                if hour <= 10.50:
                                                    return 'Cloudy'
                                                else:  # hour > 10.50
                                                    return 'Cloudy'
                                    else:  # temp > -4.25
                                        if dew_point <= -2.38:
                                            if dew_point <= -7.76:
                                                if dew_point <= -8.31:
                                                    return 'Cloudy'
                                                else:  # dew_point > -8.31
                                                    return 'Clear'
                                            else:  # dew_point > -7.76
                                                if month <= 2.50:
                                                    return 'Cloudy'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                        else:  # dew_point > -2.38
                                            if pres <= 1039.05:
                                                return 'Clear'
                                            else:  # pres > 1039.05
                                                return 'Clear'
                                else:  # pres > 1042.15
                                    if pres <= 1046.75:
                                        if pres <= 1044.35:
                                            if month <= 1.50:
                                                return 'Cloudy'
                                            else:  # month > 1.50
                                                if temp <= -10.10:
                                                    return 'Cloudy'
                                                else:  # temp > -10.10
                                                    return 'Clear'
                                        else:  # pres > 1044.35
                                            if pres <= 1044.55:
                                                if temp <= -11.35:
                                                    return 'Cloudy'
                                                else:  # temp > -11.35
                                                    return 'Clear'
                                            else:  # pres > 1044.55
                                                return 'Clear'
                                    else:  # pres > 1046.75
                                        if dew_point <= -13.03:
                                            return 'Clear'
                                        else:  # dew_point > -13.03
                                            if rhum <= 72.50:
                                                return 'Clear'
                                            else:  # rhum > 72.50
                                                if hour <= 3.50:
                                                    return 'Cloudy'
                                                else:  # hour > 3.50
                                                    return 'Cloudy'
                            else:  # latitude > 59.95
                                if rhum <= 88.00:
                                    if month <= 11.50:
                                        if hour <= 1.50:
                                            if pres <= 1038.10:
                                                return 'Rain'
                                            else:  # pres > 1038.10
                                                return 'Clear'
                                        else:  # hour > 1.50
                                            if hour <= 3.50:
                                                if rhum <= 73.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 73.50
                                                    return 'Clear'
                                            else:  # hour > 3.50
                                                if temp <= -4.50:
                                                    return 'Cloudy'
                                                else:  # temp > -4.50
                                                    return 'Cloudy'
                                    else:  # month > 11.50
                                        if dew_point <= -9.06:
                                            return 'Clear'
                                        else:  # dew_point > -9.06
                                            return 'Clear'
                                else:  # rhum > 88.00
                                    if temp <= -2.50:
                                        return 'Clear'
                                    else:  # temp > -2.50
                                        if hour <= 21.50:
                                            if rhum <= 92.50:
                                                if temp <= -1.20:
                                                    return 'Fog'
                                                else:  # temp > -1.20
                                                    return 'Cloudy'
                                            else:  # rhum > 92.50
                                                if pres <= 1043.35:
                                                    return 'Fog'
                                                else:  # pres > 1043.35
                                                    return 'Clear'
                                        else:  # hour > 21.50
                                            if dew_point <= 0.99:
                                                return 'Cloudy'
                                            else:  # dew_point > 0.99
                                                return 'Cloudy'
                else:  # dew_point > 1.04
                    if pres <= 1017.55:
                        if temp <= 2.05:
                            if month <= 2.50:
                                if hour <= 0.50:
                                    if latitude <= 59.95:
                                        return 'Rain'
                                    else:  # latitude > 59.95
                                        return 'Snow'
                                else:  # hour > 0.50
                                    if pres <= 1009.20:
                                        if rhum <= 94.50:
                                            return 'Cloudy'
                                        else:  # rhum > 94.50
                                            if rhum <= 95.50:
                                                return 'Rain'
                                            else:  # rhum > 95.50
                                                return 'Rain'
                                    else:  # pres > 1009.20
                                        if hour <= 14.50:
                                            return 'Cloudy'
                                        else:  # hour > 14.50
                                            if rhum <= 95.00:
                                                return 'Cloudy'
                                            else:  # rhum > 95.00
                                                return 'Rain'
                            else:  # month > 2.50
                                if pres <= 984.95:
                                    return 'Rain'
                                else:  # pres > 984.95
                                    if hour <= 1.50:
                                        if pres <= 1008.90:
                                            if dew_point <= 1.11:
                                                return 'Clear'
                                            else:  # dew_point > 1.11
                                                return 'Rain'
                                        else:  # pres > 1008.90
                                            if dew_point <= 1.64:
                                                return 'Clear'
                                            else:  # dew_point > 1.64
                                                return 'Cloudy'
                                    else:  # hour > 1.50
                                        if pres <= 1007.90:
                                            if hour <= 7.00:
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                            else:  # hour > 7.00
                                                if hour <= 21.00:
                                                    return 'Snow'
                                                else:  # hour > 21.00
                                                    return 'Rain'
                                        else:  # pres > 1007.90
                                            if pres <= 1016.65:
                                                if dew_point <= 1.95:
                                                    return 'Snow'
                                                else:  # dew_point > 1.95
                                                    return 'Fog'
                                            else:  # pres > 1016.65
                                                if dew_point <= 1.74:
                                                    return 'Rain'
                                                else:  # dew_point > 1.74
                                                    return 'Snow'
                        else:  # temp > 2.05
                            if dew_point <= 1.58:
                                if pres <= 1005.90:
                                    if hour <= 6.50:
                                        if hour <= 0.50:
                                            if month <= 5.50:
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Snow'
                                            else:  # month > 5.50
                                                if pres <= 979.50:
                                                    return 'Clear'
                                                else:  # pres > 979.50
                                                    return 'Rain'
                                        else:  # hour > 0.50
                                            if pres <= 1001.10:
                                                if dew_point <= 1.16:
                                                    return 'Rain'
                                                else:  # dew_point > 1.16
                                                    return 'Rain'
                                            else:  # pres > 1001.10
                                                if month <= 7.00:
                                                    return 'Rain'
                                                else:  # month > 7.00
                                                    return 'Cloudy'
                                    else:  # hour > 6.50
                                        if hour <= 7.50:
                                            if pres <= 994.55:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Snow'
                                            else:  # pres > 994.55
                                                if pres <= 1001.00:
                                                    return 'Rain'
                                                else:  # pres > 1001.00
                                                    return 'Clear'
                                        else:  # hour > 7.50
                                            if pres <= 981.50:
                                                if hour <= 21.00:
                                                    return 'Rain'
                                                else:  # hour > 21.00
                                                    return 'Rain'
                                            else:  # pres > 981.50
                                                if pres <= 986.45:
                                                    return 'Snow'
                                                else:  # pres > 986.45
                                                    return 'Rain'
                                else:  # pres > 1005.90
                                    if pres <= 1007.65:
                                        if hour <= 9.50:
                                            if temp <= 2.35:
                                                return 'Rain'
                                            else:  # temp > 2.35
                                                if dew_point <= 1.55:
                                                    return 'Cloudy'
                                                else:  # dew_point > 1.55
                                                    return 'Rain'
                                        else:  # hour > 9.50
                                            if rhum <= 93.50:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Snow'
                                            else:  # rhum > 93.50
                                                if temp <= 2.20:
                                                    return 'Cloudy'
                                                else:  # temp > 2.20
                                                    return 'Cloudy'
                                    else:  # pres > 1007.65
                                        if temp <= 2.85:
                                            if month <= 7.00:
                                                if month <= 1.50:
                                                    return 'Cloudy'
                                                else:  # month > 1.50
                                                    return 'Rain'
                                            else:  # month > 7.00
                                                if dew_point <= 1.40:
                                                    return 'Cloudy'
                                                else:  # dew_point > 1.40
                                                    return 'Rain'
                                        else:  # temp > 2.85
                                            if hour <= 16.50:
                                                if hour <= 11.50:
                                                    return 'Snow'
                                                else:  # hour > 11.50
                                                    return 'Snow'
                                            else:  # hour > 16.50
                                                if pres <= 1011.85:
                                                    return 'Rain'
                                                else:  # pres > 1011.85
                                                    return 'Cloudy'
                            else:  # dew_point > 1.58
                                if latitude <= 59.95:
                                    if pres <= 1012.10:
                                        if dew_point <= 1.63:
                                            if dew_point <= 1.58:
                                                return 'Rain'
                                            else:  # dew_point > 1.58
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Cloudy'
                                        else:  # dew_point > 1.63
                                            if pres <= 985.65:
                                                if rhum <= 93.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 93.50
                                                    return 'Rain'
                                            else:  # pres > 985.65
                                                if hour <= 20.50:
                                                    return 'Rain'
                                                else:  # hour > 20.50
                                                    return 'Rain'
                                    else:  # pres > 1012.10
                                        if pres <= 1013.05:
                                            return 'Cloudy'
                                        else:  # pres > 1013.05
                                            if hour <= 2.50:
                                                return 'Cloudy'
                                            else:  # hour > 2.50
                                                if month <= 3.50:
                                                    return 'Rain'
                                                else:  # month > 3.50
                                                    return 'Cloudy'
                                else:  # latitude > 59.95
                                    if month <= 7.00:
                                        if hour <= 1.50:
                                            if month <= 3.50:
                                                return 'Rain'
                                            else:  # month > 3.50
                                                if pres <= 999.00:
                                                    return 'Rain'
                                                else:  # pres > 999.00
                                                    return 'Cloudy'
                                        else:  # hour > 1.50
                                            if month <= 2.50:
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Cloudy'
                                            else:  # month > 2.50
                                                if hour <= 22.50:
                                                    return 'Rain'
                                                else:  # hour > 22.50
                                                    return 'Rain'
                                    else:  # month > 7.00
                                        if pres <= 991.40:
                                            if month <= 10.00:
                                                return 'Cloudy'
                                            else:  # month > 10.00
                                                return 'Rain'
                                        else:  # pres > 991.40
                                            if hour <= 8.50:
                                                if hour <= 3.50:
                                                    return 'Rain'
                                                else:  # hour > 3.50
                                                    return 'Snow'
                                            else:  # hour > 8.50
                                                if hour <= 10.50:
                                                    return 'Fog'
                                                else:  # hour > 10.50
                                                    return 'Rain'
                    else:  # pres > 1017.55
                        if dew_point <= 1.98:
                            if pres <= 1021.30:
                                if dew_point <= 1.17:
                                    if month <= 9.50:
                                        if pres <= 1017.95:
                                            return 'Rain'
                                        else:  # pres > 1017.95
                                            if month <= 7.00:
                                                if pres <= 1018.05:
                                                    return 'Clear'
                                                else:  # pres > 1018.05
                                                    return 'Cloudy'
                                            else:  # month > 7.00
                                                return 'Clear'
                                    else:  # month > 9.50
                                        if hour <= 17.00:
                                            if latitude <= 59.95:
                                                if dew_point <= 1.07:
                                                    return 'Cloudy'
                                                else:  # dew_point > 1.07
                                                    return 'Clear'
                                            else:  # latitude > 59.95
                                                return 'Snow'
                                        else:  # hour > 17.00
                                            if hour <= 20.50:
                                                return 'Cloudy'
                                            else:  # hour > 20.50
                                                return 'Clear'
                                else:  # dew_point > 1.17
                                    if rhum <= 92.50:
                                        if pres <= 1018.65:
                                            if pres <= 1018.25:
                                                return 'Cloudy'
                                            else:  # pres > 1018.25
                                                return 'Clear'
                                        else:  # pres > 1018.65
                                            return 'Cloudy'
                                    else:  # rhum > 92.50
                                        if pres <= 1019.10:
                                            if hour <= 16.50:
                                                if hour <= 5.50:
                                                    return 'Cloudy'
                                                else:  # hour > 5.50
                                                    return 'Cloudy'
                                            else:  # hour > 16.50
                                                return 'Rain'
                                        else:  # pres > 1019.10
                                            if rhum <= 94.50:
                                                if temp <= 2.80:
                                                    return 'Rain'
                                                else:  # temp > 2.80
                                                    return 'Rain'
                                            else:  # rhum > 94.50
                                                if month <= 3.50:
                                                    return 'Cloudy'
                                                else:  # month > 3.50
                                                    return 'Clear'
                            else:  # pres > 1021.30
                                if hour <= 5.50:
                                    if rhum <= 95.50:
                                        if pres <= 1024.20:
                                            if pres <= 1023.55:
                                                if month <= 2.00:
                                                    return 'Rain'
                                                else:  # month > 2.00
                                                    return 'Cloudy'
                                            else:  # pres > 1023.55
                                                if month <= 6.50:
                                                    return 'Rain'
                                                else:  # month > 6.50
                                                    return 'Clear'
                                        else:  # pres > 1024.20
                                            if rhum <= 88.00:
                                                if hour <= 3.00:
                                                    return 'Clear'
                                                else:  # hour > 3.00
                                                    return 'Cloudy'
                                            else:  # rhum > 88.00
                                                if pres <= 1030.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1030.50
                                                    return 'Cloudy'
                                    else:  # rhum > 95.50
                                        if pres <= 1036.35:
                                            return 'Clear'
                                        else:  # pres > 1036.35
                                            return 'Cloudy'
                                else:  # hour > 5.50
                                    if month <= 2.00:
                                        if hour <= 6.50:
                                            return 'Cloudy'
                                        else:  # hour > 6.50
                                            return 'Rain'
                                    else:  # month > 2.00
                                        if hour <= 16.50:
                                            if temp <= 2.30:
                                                if month <= 11.50:
                                                    return 'Cloudy'
                                                else:  # month > 11.50
                                                    return 'Clear'
                                            else:  # temp > 2.30
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Cloudy'
                                        else:  # hour > 16.50
                                            if dew_point <= 1.87:
                                                if dew_point <= 1.67:
                                                    return 'Cloudy'
                                                else:  # dew_point > 1.67
                                                    return 'Cloudy'
                                            else:  # dew_point > 1.87
                                                if pres <= 1030.40:
                                                    return 'Rain'
                                                else:  # pres > 1030.40
                                                    return 'Cloudy'
                        else:  # dew_point > 1.98
                            if latitude <= 59.95:
                                if month <= 9.50:
                                    return 'Clear'
                                else:  # month > 9.50
                                    if rhum <= 99.50:
                                        if pres <= 1024.30:
                                            return 'Cloudy'
                                        else:  # pres > 1024.30
                                            if pres <= 1028.70:
                                                return 'Clear'
                                            else:  # pres > 1028.70
                                                return 'Cloudy'
                                    else:  # rhum > 99.50
                                        if pres <= 1021.25:
                                            return 'Clear'
                                        else:  # pres > 1021.25
                                            return 'Clear'
                            else:  # latitude > 59.95
                                if hour <= 22.50:
                                    if hour <= 5.50:
                                        if pres <= 1035.50:
                                            if pres <= 1029.50:
                                                return 'Rain'
                                            else:  # pres > 1029.50
                                                return 'Clear'
                                        else:  # pres > 1035.50
                                            return 'Fog'
                                    else:  # hour > 5.50
                                        if rhum <= 97.50:
                                            return 'Fog'
                                        else:  # rhum > 97.50
                                            if pres <= 1024.00:
                                                return 'Cloudy'
                                            else:  # pres > 1024.00
                                                if pres <= 1038.00:
                                                    return 'Fog'
                                                else:  # pres > 1038.00
                                                    return 'Fog'
                                else:  # hour > 22.50
                                    if month <= 11.50:
                                        return 'Cloudy'
                                    else:  # month > 11.50
                                        return 'Cloudy'
    else:  # temp > 3.05
        if dew_point <= 21.83:
            if rhum <= 74.50:
                if latitude <= 42.48:
                    if latitude <= 15.70:
                        if dew_point <= 13.65:
                            if dew_point <= 6.80:
                                if dew_point <= 5.94:
                                    if temp <= 36.60:
                                        if rhum <= 55.50:
                                            if dew_point <= 4.89:
                                                if rhum <= 43.50:
                                                    return 'Clear'
                                                else:  # rhum > 43.50
                                                    return 'Clear'
                                            else:  # dew_point > 4.89
                                                if pres <= 999.50:
                                                    return 'Rain'
                                                else:  # pres > 999.50
                                                    return 'Clear'
                                        else:  # rhum > 55.50
                                            if pres <= 1018.05:
                                                if latitude <= -28.71:
                                                    return 'Clear'
                                                else:  # latitude > -28.71
                                                    return 'Clear'
                                            else:  # pres > 1018.05
                                                if rhum <= 62.50:
                                                    return 'Clear'
                                                else:  # rhum > 62.50
                                                    return 'Clear'
                                    else:  # temp > 36.60
                                        if pres <= 1003.75:
                                            return 'Clear'
                                        else:  # pres > 1003.75
                                            if pres <= 1009.90:
                                                return 'Fog'
                                            else:  # pres > 1009.90
                                                return 'Clear'
                                else:  # dew_point > 5.94
                                    if pres <= 1017.75:
                                        if rhum <= 55.50:
                                            if pres <= 1000.20:
                                                if temp <= 19.40:
                                                    return 'Clear'
                                                else:  # temp > 19.40
                                                    return 'Rain'
                                            else:  # pres > 1000.20
                                                if month <= 4.50:
                                                    return 'Clear'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                        else:  # rhum > 55.50
                                            if hour <= 8.50:
                                                if latitude <= -28.71:
                                                    return 'Rain'
                                                else:  # latitude > -28.71
                                                    return 'Clear'
                                            else:  # hour > 8.50
                                                if month <= 5.50:
                                                    return 'Clear'
                                                else:  # month > 5.50
                                                    return 'Clear'
                                    else:  # pres > 1017.75
                                        if month <= 9.50:
                                            if pres <= 1026.35:
                                                if temp <= 10.45:
                                                    return 'Rain'
                                                else:  # temp > 10.45
                                                    return 'Clear'
                                            else:  # pres > 1026.35
                                                if month <= 6.50:
                                                    return 'Clear'
                                                else:  # month > 6.50
                                                    return 'Clear'
                                        else:  # month > 9.50
                                            if rhum <= 50.50:
                                                if pres <= 1027.50:
                                                    return 'Clear'
                                                else:  # pres > 1027.50
                                                    return 'Rain'
                                            else:  # rhum > 50.50
                                                if dew_point <= 6.72:
                                                    return 'Cloudy'
                                                else:  # dew_point > 6.72
                                                    return 'Clear'
                            else:  # dew_point > 6.80
                                if rhum <= 52.50:
                                    if pres <= 1012.25:
                                        if dew_point <= 11.61:
                                            if latitude <= -28.71:
                                                if month <= 3.50:
                                                    return 'Clear'
                                                else:  # month > 3.50
                                                    return 'Clear'
                                            else:  # latitude > -28.71
                                                if month <= 5.50:
                                                    return 'Clear'
                                                else:  # month > 5.50
                                                    return 'Clear'
                                        else:  # dew_point > 11.61
                                            if rhum <= 50.50:
                                                if hour <= 14.50:
                                                    return 'Clear'
                                                else:  # hour > 14.50
                                                    return 'Clear'
                                            else:  # rhum > 50.50
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Storm'
                                    else:  # pres > 1012.25
                                        if month <= 5.50:
                                            if latitude <= -28.71:
                                                if month <= 2.50:
                                                    return 'Clear'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                            else:  # latitude > -28.71
                                                if temp <= 25.35:
                                                    return 'Clear'
                                                else:  # temp > 25.35
                                                    return 'Clear'
                                        else:  # month > 5.50
                                            if month <= 11.50:
                                                if pres <= 1018.85:
                                                    return 'Clear'
                                                else:  # pres > 1018.85
                                                    return 'Clear'
                                            else:  # month > 11.50
                                                if pres <= 1020.30:
                                                    return 'Clear'
                                                else:  # pres > 1020.30
                                                    return 'Cloudy'
                                else:  # rhum > 52.50
                                    if month <= 9.50:
                                        if month <= 2.50:
                                            if pres <= 1015.85:
                                                if latitude <= -28.71:
                                                    return 'Clear'
                                                else:  # latitude > -28.71
                                                    return 'Clear'
                                            else:  # pres > 1015.85
                                                if temp <= 18.65:
                                                    return 'Clear'
                                                else:  # temp > 18.65
                                                    return 'Cloudy'
                                        else:  # month > 2.50
                                            if month <= 5.50:
                                                if latitude <= -28.71:
                                                    return 'Clear'
                                                else:  # latitude > -28.71
                                                    return 'Rain'
                                            else:  # month > 5.50
                                                if latitude <= -28.71:
                                                    return 'Clear'
                                                else:  # latitude > -28.71
                                                    return 'Clear'
                                    else:  # month > 9.50
                                        if pres <= 1003.55:
                                            if hour <= 5.50:
                                                if hour <= 4.50:
                                                    return 'Rain'
                                                else:  # hour > 4.50
                                                    return 'Storm'
                                            else:  # hour > 5.50
                                                if hour <= 9.50:
                                                    return 'Rain'
                                                else:  # hour > 9.50
                                                    return 'Clear'
                                        else:  # pres > 1003.55
                                            if pres <= 1015.05:
                                                if temp <= 16.95:
                                                    return 'Rain'
                                                else:  # temp > 16.95
                                                    return 'Clear'
                                            else:  # pres > 1015.05
                                                if month <= 11.50:
                                                    return 'Cloudy'
                                                else:  # month > 11.50
                                                    return 'Cloudy'
                        else:  # dew_point > 13.65
                            if pres <= 1008.15:
                                if hour <= 11.50:
                                    if temp <= 24.95:
                                        if temp <= 20.60:
                                            if pres <= 1003.75:
                                                return 'Storm'
                                            else:  # pres > 1003.75
                                                if latitude <= -28.71:
                                                    return 'Cloudy'
                                                else:  # latitude > -28.71
                                                    return 'Clear'
                                        else:  # temp > 20.60
                                            if month <= 3.50:
                                                if month <= 1.50:
                                                    return 'Cloudy'
                                                else:  # month > 1.50
                                                    return 'Clear'
                                            else:  # month > 3.50
                                                if rhum <= 60.50:
                                                    return 'Clear'
                                                else:  # rhum > 60.50
                                                    return 'Rain'
                                    else:  # temp > 24.95
                                        if hour <= 4.50:
                                            if pres <= 1005.15:
                                                if hour <= 1.50:
                                                    return 'Clear'
                                                else:  # hour > 1.50
                                                    return 'Storm'
                                            else:  # pres > 1005.15
                                                if rhum <= 54.50:
                                                    return 'Clear'
                                                else:  # rhum > 54.50
                                                    return 'Rain'
                                        else:  # hour > 4.50
                                            if pres <= 997.70:
                                                if dew_point <= 17.27:
                                                    return 'Rain'
                                                else:  # dew_point > 17.27
                                                    return 'Clear'
                                            else:  # pres > 997.70
                                                if pres <= 1007.25:
                                                    return 'Storm'
                                                else:  # pres > 1007.25
                                                    return 'Storm'
                                else:  # hour > 11.50
                                    if latitude <= -28.71:
                                        if pres <= 989.15:
                                            return 'Rain'
                                        else:  # pres > 989.15
                                            if temp <= 23.65:
                                                if pres <= 1006.65:
                                                    return 'Clear'
                                                else:  # pres > 1006.65
                                                    return 'Rain'
                                            else:  # temp > 23.65
                                                if rhum <= 40.00:
                                                    return 'Rain'
                                                else:  # rhum > 40.00
                                                    return 'Clear'
                                    else:  # latitude > -28.71
                                        if month <= 3.50:
                                            if hour <= 12.50:
                                                if rhum <= 64.00:
                                                    return 'Rain'
                                                else:  # rhum > 64.00
                                                    return 'Cloudy'
                                            else:  # hour > 12.50
                                                if hour <= 15.50:
                                                    return 'Rain'
                                                else:  # hour > 15.50
                                                    return 'Rain'
                                        else:  # month > 3.50
                                            if hour <= 14.50:
                                                if dew_point <= 15.62:
                                                    return 'Clear'
                                                else:  # dew_point > 15.62
                                                    return 'Cloudy'
                                            else:  # hour > 14.50
                                                if dew_point <= 16.52:
                                                    return 'Cloudy'
                                                else:  # dew_point > 16.52
                                                    return 'Rain'
                            else:  # pres > 1008.15
                                if latitude <= -28.71:
                                    if rhum <= 60.50:
                                        if pres <= 1010.85:
                                            if pres <= 1009.35:
                                                if hour <= 4.50:
                                                    return 'Clear'
                                                else:  # hour > 4.50
                                                    return 'Clear'
                                            else:  # pres > 1009.35
                                                if month <= 10.50:
                                                    return 'Storm'
                                                else:  # month > 10.50
                                                    return 'Clear'
                                        else:  # pres > 1010.85
                                            if rhum <= 52.50:
                                                if temp <= 26.65:
                                                    return 'Clear'
                                                else:  # temp > 26.65
                                                    return 'Clear'
                                            else:  # rhum > 52.50
                                                if pres <= 1016.05:
                                                    return 'Clear'
                                                else:  # pres > 1016.05
                                                    return 'Clear'
                                    else:  # rhum > 60.50
                                        if hour <= 6.50:
                                            if pres <= 1010.55:
                                                if hour <= 3.50:
                                                    return 'Rain'
                                                else:  # hour > 3.50
                                                    return 'Storm'
                                            else:  # pres > 1010.55
                                                if dew_point <= 19.73:
                                                    return 'Cloudy'
                                                else:  # dew_point > 19.73
                                                    return 'Storm'
                                        else:  # hour > 6.50
                                            if temp <= 22.45:
                                                if month <= 2.50:
                                                    return 'Cloudy'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                            else:  # temp > 22.45
                                                if rhum <= 71.50:
                                                    return 'Clear'
                                                else:  # rhum > 71.50
                                                    return 'Clear'
                                else:  # latitude > -28.71
                                    if latitude <= -11.10:
                                        if month <= 5.50:
                                            if hour <= 19.50:
                                                if dew_point <= 19.03:
                                                    return 'Rain'
                                                else:  # dew_point > 19.03
                                                    return 'Rain'
                                            else:  # hour > 19.50
                                                if month <= 2.50:
                                                    return 'Storm'
                                                else:  # month > 2.50
                                                    return 'Rain'
                                        else:  # month > 5.50
                                            if month <= 11.50:
                                                if dew_point <= 16.09:
                                                    return 'Clear'
                                                else:  # dew_point > 16.09
                                                    return 'Cloudy'
                                            else:  # month > 11.50
                                                if dew_point <= 15.87:
                                                    return 'Cloudy'
                                                else:  # dew_point > 15.87
                                                    return 'Rain'
                                    else:  # latitude > -11.10
                                        if month <= 8.50:
                                            if pres <= 1009.85:
                                                if hour <= 9.50:
                                                    return 'Storm'
                                                else:  # hour > 9.50
                                                    return 'Cloudy'
                                            else:  # pres > 1009.85
                                                if month <= 5.00:
                                                    return 'Cloudy'
                                                else:  # month > 5.00
                                                    return 'Rain'
                                        else:  # month > 8.50
                                            if hour <= 6.50:
                                                if temp <= 29.50:
                                                    return 'Rain'
                                                else:  # temp > 29.50
                                                    return 'Cloudy'
                                            else:  # hour > 6.50
                                                if dew_point <= 20.91:
                                                    return 'Cloudy'
                                                else:  # dew_point > 20.91
                                                    return 'Storm'
                    else:  # latitude > 15.70
                        if latitude <= 34.10:
                            if temp <= 23.95:
                                if latitude <= 31.28:
                                    if month <= 9.50:
                                        if month <= 2.50:
                                            if rhum <= 51.50:
                                                if hour <= 8.50:
                                                    return 'Fog'
                                                else:  # hour > 8.50
                                                    return 'Clear'
                                            else:  # rhum > 51.50
                                                if hour <= 15.50:
                                                    return 'Fog'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                        else:  # month > 2.50
                                            if hour <= 15.50:
                                                if hour <= 8.50:
                                                    return 'Clear'
                                                else:  # hour > 8.50
                                                    return 'Clear'
                                            else:  # hour > 15.50
                                                if hour <= 19.50:
                                                    return 'Clear'
                                                else:  # hour > 19.50
                                                    return 'Clear'
                                    else:  # month > 9.50
                                        if hour <= 10.50:
                                            if temp <= 21.15:
                                                if temp <= 11.60:
                                                    return 'Clear'
                                                else:  # temp > 11.60
                                                    return 'Fog'
                                            else:  # temp > 21.15
                                                if pres <= 1014.75:
                                                    return 'Clear'
                                                else:  # pres > 1014.75
                                                    return 'Fog'
                                        else:  # hour > 10.50
                                            if pres <= 1013.95:
                                                if pres <= 1010.45:
                                                    return 'Fog'
                                                else:  # pres > 1010.45
                                                    return 'Clear'
                                            else:  # pres > 1013.95
                                                if pres <= 1019.55:
                                                    return 'Fog'
                                                else:  # pres > 1019.55
                                                    return 'Clear'
                                else:  # latitude > 31.28
                                    if dew_point <= 2.18:
                                        if pres <= 1018.25:
                                            if month <= 1.50:
                                                if temp <= 8.15:
                                                    return 'Fog'
                                                else:  # temp > 8.15
                                                    return 'Clear'
                                            else:  # month > 1.50
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Clear'
                                        else:  # pres > 1018.25
                                            if temp <= 11.60:
                                                if temp <= 11.20:
                                                    return 'Clear'
                                                else:  # temp > 11.20
                                                    return 'Fog'
                                            else:  # temp > 11.60
                                                if rhum <= 9.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 9.50
                                                    return 'Clear'
                                    else:  # dew_point > 2.18
                                        if hour <= 16.50:
                                            if hour <= 5.50:
                                                if temp <= 22.05:
                                                    return 'Clear'
                                                else:  # temp > 22.05
                                                    return 'Fog'
                                            else:  # hour > 5.50
                                                if month <= 8.50:
                                                    return 'Fog'
                                                else:  # month > 8.50
                                                    return 'Fog'
                                        else:  # hour > 16.50
                                            if rhum <= 69.50:
                                                if rhum <= 45.50:
                                                    return 'Clear'
                                                else:  # rhum > 45.50
                                                    return 'Cloudy'
                                            else:  # rhum > 69.50
                                                if temp <= 16.90:
                                                    return 'Fog'
                                                else:  # temp > 16.90
                                                    return 'Cloudy'
                            else:  # temp > 23.95
                                if temp <= 30.15:
                                    if latitude <= 31.28:
                                        if hour <= 9.50:
                                            if month <= 4.50:
                                                if rhum <= 15.50:
                                                    return 'Clear'
                                                else:  # rhum > 15.50
                                                    return 'Fog'
                                            else:  # month > 4.50
                                                if dew_point <= 21.00:
                                                    return 'Clear'
                                                else:  # dew_point > 21.00
                                                    return 'Fog'
                                        else:  # hour > 9.50
                                            if month <= 10.50:
                                                if month <= 4.50:
                                                    return 'Clear'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                            else:  # month > 10.50
                                                if pres <= 1013.75:
                                                    return 'Clear'
                                                else:  # pres > 1013.75
                                                    return 'Fog'
                                    else:  # latitude > 31.28
                                        if month <= 8.50:
                                            if pres <= 1014.35:
                                                if rhum <= 32.50:
                                                    return 'Fog'
                                                else:  # rhum > 32.50
                                                    return 'Clear'
                                            else:  # pres > 1014.35
                                                if dew_point <= 16.75:
                                                    return 'Clear'
                                                else:  # dew_point > 16.75
                                                    return 'Clear'
                                        else:  # month > 8.50
                                            if rhum <= 39.50:
                                                if pres <= 1014.70:
                                                    return 'Fog'
                                                else:  # pres > 1014.70
                                                    return 'Clear'
                                            else:  # rhum > 39.50
                                                if rhum <= 67.50:
                                                    return 'Fog'
                                                else:  # rhum > 67.50
                                                    return 'Clear'
                                else:  # temp > 30.15
                                    if hour <= 7.50:
                                        if month <= 5.50:
                                            if pres <= 1006.95:
                                                return 'Clear'
                                            else:  # pres > 1006.95
                                                if rhum <= 16.50:
                                                    return 'Fog'
                                                else:  # rhum > 16.50
                                                    return 'Fog'
                                        else:  # month > 5.50
                                            if dew_point <= 17.40:
                                                if pres <= 1003.45:
                                                    return 'Cloudy'
                                                else:  # pres > 1003.45
                                                    return 'Clear'
                                            else:  # dew_point > 17.40
                                                if hour <= 5.50:
                                                    return 'Clear'
                                                else:  # hour > 5.50
                                                    return 'Fog'
                                    else:  # hour > 7.50
                                        if month <= 9.50:
                                            if dew_point <= 19.01:
                                                if month <= 4.50:
                                                    return 'Clear'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                            else:  # dew_point > 19.01
                                                if hour <= 12.50:
                                                    return 'Clear'
                                                else:  # hour > 12.50
                                                    return 'Clear'
                                        else:  # month > 9.50
                                            if dew_point <= 16.74:
                                                if hour <= 11.50:
                                                    return 'Fog'
                                                else:  # hour > 11.50
                                                    return 'Clear'
                                            else:  # dew_point > 16.74
                                                if pres <= 1011.15:
                                                    return 'Fog'
                                                else:  # pres > 1011.15
                                                    return 'Clear'
                        else:  # latitude > 34.10
                            if rhum <= 64.50:
                                if month <= 1.50:
                                    if pres <= 1007.85:
                                        if temp <= 6.55:
                                            if dew_point <= -6.44:
                                                if dew_point <= -16.33:
                                                    return 'Clear'
                                                else:  # dew_point > -16.33
                                                    return 'Clear'
                                            else:  # dew_point > -6.44
                                                if pres <= 1003.05:
                                                    return 'Clear'
                                                else:  # pres > 1003.05
                                                    return 'Snow'
                                        else:  # temp > 6.55
                                            return 'Clear'
                                    else:  # pres > 1007.85
                                        if rhum <= 52.50:
                                            if pres <= 1010.05:
                                                if pres <= 1009.95:
                                                    return 'Clear'
                                                else:  # pres > 1009.95
                                                    return 'Snow'
                                            else:  # pres > 1010.05
                                                if hour <= 22.50:
                                                    return 'Clear'
                                                else:  # hour > 22.50
                                                    return 'Clear'
                                        else:  # rhum > 52.50
                                            if dew_point <= -3.06:
                                                if hour <= 6.00:
                                                    return 'Snow'
                                                else:  # hour > 6.00
                                                    return 'Clear'
                                            else:  # dew_point > -3.06
                                                if dew_point <= -0.35:
                                                    return 'Clear'
                                                else:  # dew_point > -0.35
                                                    return 'Clear'
                                else:  # month > 1.50
                                    if rhum <= 59.50:
                                        if rhum <= 53.50:
                                            if rhum <= 49.50:
                                                if month <= 2.50:
                                                    return 'Clear'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                            else:  # rhum > 49.50
                                                if pres <= 998.65:
                                                    return 'Clear'
                                                else:  # pres > 998.65
                                                    return 'Clear'
                                        else:  # rhum > 53.50
                                            if month <= 4.50:
                                                if pres <= 1009.35:
                                                    return 'Clear'
                                                else:  # pres > 1009.35
                                                    return 'Clear'
                                            else:  # month > 4.50
                                                if dew_point <= 0.35:
                                                    return 'Clear'
                                                else:  # dew_point > 0.35
                                                    return 'Clear'
                                    else:  # rhum > 59.50
                                        if pres <= 1001.25:
                                            if hour <= 5.50:
                                                return 'Clear'
                                            else:  # hour > 5.50
                                                if dew_point <= 5.24:
                                                    return 'Clear'
                                                else:  # dew_point > 5.24
                                                    return 'Rain'
                                        else:  # pres > 1001.25
                                            if hour <= 12.50:
                                                if temp <= 21.55:
                                                    return 'Clear'
                                                else:  # temp > 21.55
                                                    return 'Clear'
                                            else:  # hour > 12.50
                                                if pres <= 1003.85:
                                                    return 'Clear'
                                                else:  # pres > 1003.85
                                                    return 'Clear'
                            else:  # rhum > 64.50
                                if dew_point <= -2.31:
                                    if dew_point <= -2.41:
                                        if month <= 1.50:
                                            return 'Clear'
                                        else:  # month > 1.50
                                            return 'Clear'
                                    else:  # dew_point > -2.41
                                        if hour <= 18.00:
                                            return 'Rain'
                                        else:  # hour > 18.00
                                            if hour <= 20.50:
                                                return 'Snow'
                                            else:  # hour > 20.50
                                                return 'Clear'
                                else:  # dew_point > -2.31
                                    if hour <= 11.50:
                                        if rhum <= 68.50:
                                            if temp <= 20.45:
                                                if temp <= 14.20:
                                                    return 'Clear'
                                                else:  # temp > 14.20
                                                    return 'Clear'
                                            else:  # temp > 20.45
                                                if pres <= 1011.65:
                                                    return 'Clear'
                                                else:  # pres > 1011.65
                                                    return 'Clear'
                                        else:  # rhum > 68.50
                                            if pres <= 1002.35:
                                                if pres <= 1002.20:
                                                    return 'Clear'
                                                else:  # pres > 1002.20
                                                    return 'Storm'
                                            else:  # pres > 1002.35
                                                if month <= 7.50:
                                                    return 'Clear'
                                                else:  # month > 7.50
                                                    return 'Clear'
                                    else:  # hour > 11.50
                                        if temp <= 13.25:
                                            if month <= 2.50:
                                                if hour <= 15.50:
                                                    return 'Clear'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                            else:  # month > 2.50
                                                if pres <= 1028.75:
                                                    return 'Clear'
                                                else:  # pres > 1028.75
                                                    return 'Clear'
                                        else:  # temp > 13.25
                                            if dew_point <= 21.71:
                                                if temp <= 16.25:
                                                    return 'Clear'
                                                else:  # temp > 16.25
                                                    return 'Clear'
                                            else:  # dew_point > 21.71
                                                if pres <= 1011.45:
                                                    return 'Rain'
                                                else:  # pres > 1011.45
                                                    return 'Clear'
                else:  # latitude > 42.48
                    if dew_point <= 12.89:
                        if pres <= 1013.55:
                            if temp <= 4.85:
                                if pres <= 995.95:
                                    if dew_point <= -0.81:
                                        if month <= 1.50:
                                            if rhum <= 66.50:
                                                return 'Cloudy'
                                            else:  # rhum > 66.50
                                                if latitude <= 56.71:
                                                    return 'Cloudy'
                                                else:  # latitude > 56.71
                                                    return 'Rain'
                                        else:  # month > 1.50
                                            if hour <= 14.50:
                                                if hour <= 1.50:
                                                    return 'Cloudy'
                                                else:  # hour > 1.50
                                                    return 'Snow'
                                            else:  # hour > 14.50
                                                if month <= 9.50:
                                                    return 'Snow'
                                                else:  # month > 9.50
                                                    return 'Fog'
                                    else:  # dew_point > -0.81
                                        if pres <= 986.65:
                                            if pres <= 983.15:
                                                if dew_point <= -0.59:
                                                    return 'Rain'
                                                else:  # dew_point > -0.59
                                                    return 'Cloudy'
                                            else:  # pres > 983.15
                                                if temp <= 4.25:
                                                    return 'Rain'
                                                else:  # temp > 4.25
                                                    return 'Rain'
                                        else:  # pres > 986.65
                                            if month <= 3.50:
                                                if month <= 1.50:
                                                    return 'Cloudy'
                                                else:  # month > 1.50
                                                    return 'Clear'
                                            else:  # month > 3.50
                                                if temp <= 4.45:
                                                    return 'Clear'
                                                else:  # temp > 4.45
                                                    return 'Cloudy'
                                else:  # pres > 995.95
                                    if month <= 4.50:
                                        if hour <= 16.50:
                                            if hour <= 5.50:
                                                if pres <= 1002.65:
                                                    return 'Snow'
                                                else:  # pres > 1002.65
                                                    return 'Cloudy'
                                            else:  # hour > 5.50
                                                if pres <= 1001.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1001.95
                                                    return 'Snow'
                                        else:  # hour > 16.50
                                            if temp <= 3.15:
                                                if rhum <= 64.50:
                                                    return 'Snow'
                                                else:  # rhum > 64.50
                                                    return 'Cloudy'
                                            else:  # temp > 3.15
                                                if dew_point <= -2.13:
                                                    return 'Clear'
                                                else:  # dew_point > -2.13
                                                    return 'Cloudy'
                                    else:  # month > 4.50
                                        if month <= 11.50:
                                            if pres <= 1012.55:
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Clear'
                                            else:  # pres > 1012.55
                                                if latitude <= 59.95:
                                                    return 'Snow'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                        else:  # month > 11.50
                                            if dew_point <= -1.03:
                                                if dew_point <= -3.05:
                                                    return 'Clear'
                                                else:  # dew_point > -3.05
                                                    return 'Cloudy'
                                            else:  # dew_point > -1.03
                                                if hour <= 12.00:
                                                    return 'Snow'
                                                else:  # hour > 12.00
                                                    return 'Cloudy'
                            else:  # temp > 4.85
                                if rhum <= 57.50:
                                    if dew_point <= 10.27:
                                        if temp <= 5.45:
                                            if month <= 5.50:
                                                if pres <= 1009.55:
                                                    return 'Snow'
                                                else:  # pres > 1009.55
                                                    return 'Clear'
                                            else:  # month > 5.50
                                                if hour <= 9.50:
                                                    return 'Clear'
                                                else:  # hour > 9.50
                                                    return 'Clear'
                                        else:  # temp > 5.45
                                            if month <= 11.50:
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                            else:  # month > 11.50
                                                if dew_point <= -3.71:
                                                    return 'Cloudy'
                                                else:  # dew_point > -3.71
                                                    return 'Cloudy'
                                    else:  # dew_point > 10.27
                                        if latitude <= 53.63:
                                            if pres <= 1003.60:
                                                if temp <= 19.45:
                                                    return 'Rain'
                                                else:  # temp > 19.45
                                                    return 'Cloudy'
                                            else:  # pres > 1003.60
                                                if temp <= 25.40:
                                                    return 'Clear'
                                                else:  # temp > 25.40
                                                    return 'Clear'
                                        else:  # latitude > 53.63
                                            if hour <= 11.50:
                                                if hour <= 8.50:
                                                    return 'Clear'
                                                else:  # hour > 8.50
                                                    return 'Cloudy'
                                            else:  # hour > 11.50
                                                if hour <= 15.50:
                                                    return 'Storm'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                else:  # rhum > 57.50
                                    if pres <= 1002.35:
                                        if pres <= 994.65:
                                            if dew_point <= 3.00:
                                                if month <= 5.50:
                                                    return 'Rain'
                                                else:  # month > 5.50
                                                    return 'Rain'
                                            else:  # dew_point > 3.00
                                                if hour <= 12.50:
                                                    return 'Rain'
                                                else:  # hour > 12.50
                                                    return 'Rain'
                                        else:  # pres > 994.65
                                            if rhum <= 67.50:
                                                if hour <= 10.50:
                                                    return 'Cloudy'
                                                else:  # hour > 10.50
                                                    return 'Cloudy'
                                            else:  # rhum > 67.50
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Rain'
                                    else:  # pres > 1002.35
                                        if month <= 6.50:
                                            if temp <= 5.95:
                                                if pres <= 1004.10:
                                                    return 'Snow'
                                                else:  # pres > 1004.10
                                                    return 'Cloudy'
                                            else:  # temp > 5.95
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Cloudy'
                                        else:  # month > 6.50
                                            if latitude <= 59.95:
                                                if pres <= 1008.55:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.55
                                                    return 'Cloudy'
                                            else:  # latitude > 59.95
                                                if dew_point <= 7.11:
                                                    return 'Cloudy'
                                                else:  # dew_point > 7.11
                                                    return 'Fog'
                        else:  # pres > 1013.55
                            if rhum <= 54.50:
                                if rhum <= 38.50:
                                    if month <= 2.50:
                                        if latitude <= 52.52:
                                            if temp <= 7.50:
                                                return 'Clear'
                                            else:  # temp > 7.50
                                                return 'Rain'
                                        else:  # latitude > 52.52
                                            if hour <= 10.50:
                                                return 'Snow'
                                            else:  # hour > 10.50
                                                return 'Cloudy'
                                    else:  # month > 2.50
                                        if latitude <= 53.63:
                                            if dew_point <= 12.24:
                                                if pres <= 1015.15:
                                                    return 'Clear'
                                                else:  # pres > 1015.15
                                                    return 'Clear'
                                            else:  # dew_point > 12.24
                                                if pres <= 1020.25:
                                                    return 'Clear'
                                                else:  # pres > 1020.25
                                                    return 'Cloudy'
                                        else:  # latitude > 53.63
                                            if temp <= 19.55:
                                                if latitude <= 59.95:
                                                    return 'Clear'
                                                else:  # latitude > 59.95
                                                    return 'Clear'
                                            else:  # temp > 19.55
                                                if rhum <= 35.50:
                                                    return 'Clear'
                                                else:  # rhum > 35.50
                                                    return 'Clear'
                                else:  # rhum > 38.50
                                    if latitude <= 53.63:
                                        if dew_point <= -6.91:
                                            if pres <= 1019.55:
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Snow'
                                            else:  # pres > 1019.55
                                                if hour <= 6.50:
                                                    return 'Clear'
                                                else:  # hour > 6.50
                                                    return 'Clear'
                                        else:  # dew_point > -6.91
                                            if pres <= 1018.15:
                                                if month <= 8.50:
                                                    return 'Clear'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                            else:  # pres > 1018.15
                                                if rhum <= 48.50:
                                                    return 'Clear'
                                                else:  # rhum > 48.50
                                                    return 'Clear'
                                    else:  # latitude > 53.63
                                        if hour <= 16.50:
                                            if hour <= 8.50:
                                                if month <= 2.50:
                                                    return 'Snow'
                                                else:  # month > 2.50
                                                    return 'Clear'
                                            else:  # hour > 8.50
                                                if temp <= 4.25:
                                                    return 'Snow'
                                                else:  # temp > 4.25
                                                    return 'Cloudy'
                                        else:  # hour > 16.50
                                            if pres <= 1025.45:
                                                if rhum <= 51.50:
                                                    return 'Clear'
                                                else:  # rhum > 51.50
                                                    return 'Clear'
                                            else:  # pres > 1025.45
                                                if dew_point <= -1.95:
                                                    return 'Clear'
                                                else:  # dew_point > -1.95
                                                    return 'Clear'
                            else:  # rhum > 54.50
                                if latitude <= 59.95:
                                    if pres <= 1021.75:
                                        if hour <= 8.50:
                                            if dew_point <= 6.54:
                                                if month <= 2.50:
                                                    return 'Snow'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 6.54
                                                if temp <= 16.65:
                                                    return 'Clear'
                                                else:  # temp > 16.65
                                                    return 'Clear'
                                        else:  # hour > 8.50
                                            if hour <= 17.50:
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Cloudy'
                                            else:  # hour > 17.50
                                                if latitude <= 50.40:
                                                    return 'Cloudy'
                                                else:  # latitude > 50.40
                                                    return 'Clear'
                                    else:  # pres > 1021.75
                                        if month <= 9.50:
                                            if hour <= 9.50:
                                                if latitude <= 50.40:
                                                    return 'Clear'
                                                else:  # latitude > 50.40
                                                    return 'Clear'
                                            else:  # hour > 9.50
                                                if hour <= 18.50:
                                                    return 'Cloudy'
                                                else:  # hour > 18.50
                                                    return 'Clear'
                                        else:  # month > 9.50
                                            if latitude <= 50.40:
                                                if pres <= 1030.40:
                                                    return 'Fog'
                                                else:  # pres > 1030.40
                                                    return 'Clear'
                                            else:  # latitude > 50.40
                                                if hour <= 15.50:
                                                    return 'Cloudy'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                else:  # latitude > 59.95
                                    if temp <= 13.35:
                                        if month <= 3.50:
                                            if hour <= 12.50:
                                                if dew_point <= -1.06:
                                                    return 'Snow'
                                                else:  # dew_point > -1.06
                                                    return 'Cloudy'
                                            else:  # hour > 12.50
                                                if rhum <= 69.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 69.50
                                                    return 'Cloudy'
                                        else:  # month > 3.50
                                            if rhum <= 65.50:
                                                if month <= 5.50:
                                                    return 'Cloudy'
                                                else:  # month > 5.50
                                                    return 'Cloudy'
                                            else:  # rhum > 65.50
                                                if month <= 5.50:
                                                    return 'Cloudy'
                                                else:  # month > 5.50
                                                    return 'Cloudy'
                                    else:  # temp > 13.35
                                        if month <= 7.50:
                                            if pres <= 1015.85:
                                                if dew_point <= 7.48:
                                                    return 'Clear'
                                                else:  # dew_point > 7.48
                                                    return 'Cloudy'
                                            else:  # pres > 1015.85
                                                if pres <= 1019.80:
                                                    return 'Fog'
                                                else:  # pres > 1019.80
                                                    return 'Cloudy'
                                        else:  # month > 7.50
                                            if temp <= 14.05:
                                                if pres <= 1026.55:
                                                    return 'Cloudy'
                                                else:  # pres > 1026.55
                                                    return 'Cloudy'
                                            else:  # temp > 14.05
                                                if rhum <= 62.50:
                                                    return 'Clear'
                                                else:  # rhum > 62.50
                                                    return 'Rain'
                    else:  # dew_point > 12.89
                        if latitude <= 53.63:
                            if temp <= 23.05:
                                if latitude <= 50.40:
                                    if dew_point <= 16.80:
                                        if hour <= 17.50:
                                            if dew_point <= 14.06:
                                                if pres <= 1021.85:
                                                    return 'Clear'
                                                else:  # pres > 1021.85
                                                    return 'Fog'
                                            else:  # dew_point > 14.06
                                                if pres <= 1019.35:
                                                    return 'Clear'
                                                else:  # pres > 1019.35
                                                    return 'Cloudy'
                                        else:  # hour > 17.50
                                            if month <= 9.50:
                                                if temp <= 20.75:
                                                    return 'Cloudy'
                                                else:  # temp > 20.75
                                                    return 'Clear'
                                            else:  # month > 9.50
                                                if pres <= 1017.35:
                                                    return 'Cloudy'
                                                else:  # pres > 1017.35
                                                    return 'Fog'
                                    else:  # dew_point > 16.80
                                        if dew_point <= 16.82:
                                            if pres <= 1012.35:
                                                return 'Storm'
                                            else:  # pres > 1012.35
                                                if pres <= 1016.15:
                                                    return 'Clear'
                                                else:  # pres > 1016.15
                                                    return 'Cloudy'
                                        else:  # dew_point > 16.82
                                            if pres <= 1018.20:
                                                if dew_point <= 17.86:
                                                    return 'Clear'
                                                else:  # dew_point > 17.86
                                                    return 'Cloudy'
                                            else:  # pres > 1018.20
                                                if pres <= 1018.90:
                                                    return 'Cloudy'
                                                else:  # pres > 1018.90
                                                    return 'Clear'
                                else:  # latitude > 50.40
                                    if pres <= 1013.45:
                                        if rhum <= 63.50:
                                            if hour <= 9.50:
                                                return 'Clear'
                                            else:  # hour > 9.50
                                                if hour <= 15.50:
                                                    return 'Cloudy'
                                                else:  # hour > 15.50
                                                    return 'Cloudy'
                                        else:  # rhum > 63.50
                                            if hour <= 11.50:
                                                if dew_point <= 14.78:
                                                    return 'Cloudy'
                                                else:  # dew_point > 14.78
                                                    return 'Cloudy'
                                            else:  # hour > 11.50
                                                if hour <= 17.50:
                                                    return 'Rain'
                                                else:  # hour > 17.50
                                                    return 'Cloudy'
                                    else:  # pres > 1013.45
                                        if hour <= 9.50:
                                            if dew_point <= 12.99:
                                                return 'Cloudy'
                                            else:  # dew_point > 12.99
                                                if pres <= 1014.90:
                                                    return 'Clear'
                                                else:  # pres > 1014.90
                                                    return 'Clear'
                                        else:  # hour > 9.50
                                            if hour <= 18.50:
                                                if month <= 9.50:
                                                    return 'Cloudy'
                                                else:  # month > 9.50
                                                    return 'Clear'
                                            else:  # hour > 18.50
                                                if pres <= 1022.20:
                                                    return 'Clear'
                                                else:  # pres > 1022.20
                                                    return 'Clear'
                            else:  # temp > 23.05
                                if pres <= 1010.75:
                                    if pres <= 1010.65:
                                        if dew_point <= 17.78:
                                            if month <= 8.50:
                                                if temp <= 23.45:
                                                    return 'Cloudy'
                                                else:  # temp > 23.45
                                                    return 'Clear'
                                            else:  # month > 8.50
                                                if pres <= 1009.35:
                                                    return 'Fog'
                                                else:  # pres > 1009.35
                                                    return 'Clear'
                                        else:  # dew_point > 17.78
                                            if month <= 6.50:
                                                if hour <= 1.00:
                                                    return 'Clear'
                                                else:  # hour > 1.00
                                                    return 'Clear'
                                            else:  # month > 6.50
                                                if hour <= 3.50:
                                                    return 'Fog'
                                                else:  # hour > 3.50
                                                    return 'Clear'
                                    else:  # pres > 1010.65
                                        if temp <= 24.10:
                                            if dew_point <= 15.67:
                                                return 'Clear'
                                            else:  # dew_point > 15.67
                                                return 'Storm'
                                        else:  # temp > 24.10
                                            return 'Clear'
                                else:  # pres > 1010.75
                                    if temp <= 24.65:
                                        if hour <= 9.50:
                                            if pres <= 1013.85:
                                                if hour <= 1.50:
                                                    return 'Clear'
                                                else:  # hour > 1.50
                                                    return 'Clear'
                                            else:  # pres > 1013.85
                                                if pres <= 1014.65:
                                                    return 'Clear'
                                                else:  # pres > 1014.65
                                                    return 'Clear'
                                        else:  # hour > 9.50
                                            if pres <= 1014.05:
                                                if month <= 7.50:
                                                    return 'Clear'
                                                else:  # month > 7.50
                                                    return 'Cloudy'
                                            else:  # pres > 1014.05
                                                if rhum <= 61.50:
                                                    return 'Clear'
                                                else:  # rhum > 61.50
                                                    return 'Clear'
                                    else:  # temp > 24.65
                                        if rhum <= 48.50:
                                            if pres <= 1015.65:
                                                if dew_point <= 16.90:
                                                    return 'Clear'
                                                else:  # dew_point > 16.90
                                                    return 'Clear'
                                            else:  # pres > 1015.65
                                                if hour <= 0.50:
                                                    return 'Cloudy'
                                                else:  # hour > 0.50
                                                    return 'Clear'
                                        else:  # rhum > 48.50
                                            if month <= 7.50:
                                                if month <= 5.50:
                                                    return 'Cloudy'
                                                else:  # month > 5.50
                                                    return 'Clear'
                                            else:  # month > 7.50
                                                if dew_point <= 15.45:
                                                    return 'Clear'
                                                else:  # dew_point > 15.45
                                                    return 'Clear'
                        else:  # latitude > 53.63
                            if hour <= 10.50:
                                if pres <= 1015.05:
                                    if temp <= 25.35:
                                        if hour <= 6.50:
                                            if dew_point <= 17.13:
                                                if pres <= 1009.35:
                                                    return 'Cloudy'
                                                else:  # pres > 1009.35
                                                    return 'Clear'
                                            else:  # dew_point > 17.13
                                                if temp <= 23.35:
                                                    return 'Cloudy'
                                                else:  # temp > 23.35
                                                    return 'Clear'
                                        else:  # hour > 6.50
                                            if pres <= 1004.55:
                                                if rhum <= 65.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 65.50
                                                    return 'Rain'
                                            else:  # pres > 1004.55
                                                if dew_point <= 16.91:
                                                    return 'Cloudy'
                                                else:  # dew_point > 16.91
                                                    return 'Snow'
                                    else:  # temp > 25.35
                                        if hour <= 8.50:
                                            if month <= 6.50:
                                                if hour <= 6.50:
                                                    return 'Clear'
                                                else:  # hour > 6.50
                                                    return 'Rain'
                                            else:  # month > 6.50
                                                if temp <= 25.45:
                                                    return 'Rain'
                                                else:  # temp > 25.45
                                                    return 'Clear'
                                        else:  # hour > 8.50
                                            if rhum <= 48.50:
                                                if temp <= 28.65:
                                                    return 'Clear'
                                                else:  # temp > 28.65
                                                    return 'Clear'
                                            else:  # rhum > 48.50
                                                if pres <= 1004.50:
                                                    return 'Rain'
                                                else:  # pres > 1004.50
                                                    return 'Cloudy'
                                else:  # pres > 1015.05
                                    if hour <= 7.50:
                                        if rhum <= 62.50:
                                            if temp <= 24.55:
                                                if dew_point <= 16.32:
                                                    return 'Clear'
                                                else:  # dew_point > 16.32
                                                    return 'Rain'
                                            else:  # temp > 24.55
                                                if rhum <= 58.00:
                                                    return 'Clear'
                                                else:  # rhum > 58.00
                                                    return 'Clear'
                                        else:  # rhum > 62.50
                                            if hour <= 5.50:
                                                if pres <= 1019.55:
                                                    return 'Clear'
                                                else:  # pres > 1019.55
                                                    return 'Clear'
                                            else:  # hour > 5.50
                                                if dew_point <= 14.21:
                                                    return 'Cloudy'
                                                else:  # dew_point > 14.21
                                                    return 'Clear'
                                    else:  # hour > 7.50
                                        if temp <= 25.25:
                                            if dew_point <= 14.55:
                                                if pres <= 1021.35:
                                                    return 'Cloudy'
                                                else:  # pres > 1021.35
                                                    return 'Clear'
                                            else:  # dew_point > 14.55
                                                if pres <= 1019.35:
                                                    return 'Rain'
                                                else:  # pres > 1019.35
                                                    return 'Cloudy'
                                        else:  # temp > 25.25
                                            if pres <= 1023.55:
                                                if pres <= 1018.05:
                                                    return 'Clear'
                                                else:  # pres > 1018.05
                                                    return 'Clear'
                                            else:  # pres > 1023.55
                                                if dew_point <= 16.12:
                                                    return 'Clear'
                                                else:  # dew_point > 16.12
                                                    return 'Rain'
                            else:  # hour > 10.50
                                if hour <= 16.50:
                                    if rhum <= 43.50:
                                        if pres <= 1008.65:
                                            if dew_point <= 13.75:
                                                if rhum <= 39.50:
                                                    return 'Clear'
                                                else:  # rhum > 39.50
                                                    return 'Storm'
                                            else:  # dew_point > 13.75
                                                if month <= 7.50:
                                                    return 'Cloudy'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                        else:  # pres > 1008.65
                                            if pres <= 1011.25:
                                                if dew_point <= 13.89:
                                                    return 'Clear'
                                                else:  # dew_point > 13.89
                                                    return 'Cloudy'
                                            else:  # pres > 1011.25
                                                if temp <= 29.35:
                                                    return 'Clear'
                                                else:  # temp > 29.35
                                                    return 'Clear'
                                    else:  # rhum > 43.50
                                        if month <= 8.50:
                                            if hour <= 15.50:
                                                if month <= 6.50:
                                                    return 'Storm'
                                                else:  # month > 6.50
                                                    return 'Storm'
                                            else:  # hour > 15.50
                                                if rhum <= 64.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 64.50
                                                    return 'Storm'
                                        else:  # month > 8.50
                                            if pres <= 1008.60:
                                                if temp <= 21.15:
                                                    return 'Rain'
                                                else:  # temp > 21.15
                                                    return 'Cloudy'
                                            else:  # pres > 1008.60
                                                if dew_point <= 12.92:
                                                    return 'Cloudy'
                                                else:  # dew_point > 12.92
                                                    return 'Cloudy'
                                else:  # hour > 16.50
                                    if rhum <= 73.50:
                                        if pres <= 1011.10:
                                            if month <= 7.50:
                                                if pres <= 1000.70:
                                                    return 'Clear'
                                                else:  # pres > 1000.70
                                                    return 'Cloudy'
                                            else:  # month > 7.50
                                                if pres <= 1007.00:
                                                    return 'Cloudy'
                                                else:  # pres > 1007.00
                                                    return 'Clear'
                                        else:  # pres > 1011.10
                                            if hour <= 18.50:
                                                if rhum <= 56.50:
                                                    return 'Clear'
                                                else:  # rhum > 56.50
                                                    return 'Clear'
                                            else:  # hour > 18.50
                                                if temp <= 18.10:
                                                    return 'Rain'
                                                else:  # temp > 18.10
                                                    return 'Clear'
                                    else:  # rhum > 73.50
                                        if hour <= 17.50:
                                            if pres <= 1012.75:
                                                if temp <= 22.20:
                                                    return 'Cloudy'
                                                else:  # temp > 22.20
                                                    return 'Cloudy'
                                            else:  # pres > 1012.75
                                                if temp <= 22.00:
                                                    return 'Storm'
                                                else:  # temp > 22.00
                                                    return 'Rain'
                                        else:  # hour > 17.50
                                            if hour <= 18.50:
                                                if temp <= 18.30:
                                                    return 'Clear'
                                                else:  # temp > 18.30
                                                    return 'Cloudy'
                                            else:  # hour > 18.50
                                                if pres <= 1010.35:
                                                    return 'Clear'
                                                else:  # pres > 1010.35
                                                    return 'Clear'
            else:  # rhum > 74.50
                if latitude <= 34.10:
                    if latitude <= 15.70:
                        if rhum <= 97.50:
                            if dew_point <= 16.69:
                                if latitude <= -28.71:
                                    if rhum <= 89.50:
                                        if hour <= 8.50:
                                            if pres <= 1007.00:
                                                if temp <= 19.05:
                                                    return 'Rain'
                                                else:  # temp > 19.05
                                                    return 'Storm'
                                            else:  # pres > 1007.00
                                                if rhum <= 79.50:
                                                    return 'Rain'
                                                else:  # rhum > 79.50
                                                    return 'Rain'
                                        else:  # hour > 8.50
                                            if dew_point <= 8.67:
                                                if pres <= 1017.75:
                                                    return 'Clear'
                                                else:  # pres > 1017.75
                                                    return 'Clear'
                                            else:  # dew_point > 8.67
                                                if month <= 10.50:
                                                    return 'Rain'
                                                else:  # month > 10.50
                                                    return 'Cloudy'
                                    else:  # rhum > 89.50
                                        if hour <= 14.50:
                                            if pres <= 1020.15:
                                                if dew_point <= 11.42:
                                                    return 'Rain'
                                                else:  # dew_point > 11.42
                                                    return 'Rain'
                                            else:  # pres > 1020.15
                                                if rhum <= 94.50:
                                                    return 'Rain'
                                                else:  # rhum > 94.50
                                                    return 'Rain'
                                        else:  # hour > 14.50
                                            if dew_point <= 12.40:
                                                if temp <= 9.55:
                                                    return 'Fog'
                                                else:  # temp > 9.55
                                                    return 'Fog'
                                            else:  # dew_point > 12.40
                                                if pres <= 1020.65:
                                                    return 'Rain'
                                                else:  # pres > 1020.65
                                                    return 'Rain'
                                else:  # latitude > -28.71
                                    if hour <= 8.50:
                                        if rhum <= 82.50:
                                            if month <= 7.50:
                                                if pres <= 1013.95:
                                                    return 'Clear'
                                                else:  # pres > 1013.95
                                                    return 'Clear'
                                            else:  # month > 7.50
                                                if hour <= 2.50:
                                                    return 'Clear'
                                                else:  # hour > 2.50
                                                    return 'Cloudy'
                                        else:  # rhum > 82.50
                                            if rhum <= 95.50:
                                                if hour <= 2.50:
                                                    return 'Cloudy'
                                                else:  # hour > 2.50
                                                    return 'Cloudy'
                                            else:  # rhum > 95.50
                                                if month <= 8.50:
                                                    return 'Fog'
                                                else:  # month > 8.50
                                                    return 'Cloudy'
                                    else:  # hour > 8.50
                                        if hour <= 13.50:
                                            if month <= 4.50:
                                                if rhum <= 88.50:
                                                    return 'Rain'
                                                else:  # rhum > 88.50
                                                    return 'Fog'
                                            else:  # month > 4.50
                                                if rhum <= 85.50:
                                                    return 'Fog'
                                                else:  # rhum > 85.50
                                                    return 'Fog'
                                        else:  # hour > 13.50
                                            if hour <= 19.50:
                                                if rhum <= 84.50:
                                                    return 'Rain'
                                                else:  # rhum > 84.50
                                                    return 'Rain'
                                            else:  # hour > 19.50
                                                if month <= 4.50:
                                                    return 'Rain'
                                                else:  # month > 4.50
                                                    return 'Cloudy'
                            else:  # dew_point > 16.69
                                if dew_point <= 19.86:
                                    if pres <= 1007.55:
                                        if hour <= 12.50:
                                            if latitude <= -28.71:
                                                if rhum <= 93.50:
                                                    return 'Storm'
                                                else:  # rhum > 93.50
                                                    return 'Rain'
                                            else:  # latitude > -28.71
                                                if dew_point <= 17.08:
                                                    return 'Fog'
                                                else:  # dew_point > 17.08
                                                    return 'Rain'
                                        else:  # hour > 12.50
                                            if latitude <= -28.71:
                                                if rhum <= 89.50:
                                                    return 'Clear'
                                                else:  # rhum > 89.50
                                                    return 'Rain'
                                            else:  # latitude > -28.71
                                                if hour <= 13.50:
                                                    return 'Cloudy'
                                                else:  # hour > 13.50
                                                    return 'Rain'
                                    else:  # pres > 1007.55
                                        if month <= 4.50:
                                            if hour <= 16.50:
                                                if latitude <= -28.71:
                                                    return 'Rain'
                                                else:  # latitude > -28.71
                                                    return 'Rain'
                                            else:  # hour > 16.50
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Rain'
                                        else:  # month > 4.50
                                            if month <= 9.50:
                                                if latitude <= -28.71:
                                                    return 'Rain'
                                                else:  # latitude > -28.71
                                                    return 'Fog'
                                            else:  # month > 9.50
                                                if latitude <= -28.71:
                                                    return 'Rain'
                                                else:  # latitude > -28.71
                                                    return 'Rain'
                                else:  # dew_point > 19.86
                                    if pres <= 1016.15:
                                        if month <= 1.50:
                                            if hour <= 11.50:
                                                if latitude <= -28.71:
                                                    return 'Storm'
                                                else:  # latitude > -28.71
                                                    return 'Storm'
                                            else:  # hour > 11.50
                                                if pres <= 1014.95:
                                                    return 'Storm'
                                                else:  # pres > 1014.95
                                                    return 'Storm'
                                        else:  # month > 1.50
                                            if latitude <= -11.10:
                                                if hour <= 4.50:
                                                    return 'Rain'
                                                else:  # hour > 4.50
                                                    return 'Rain'
                                            else:  # latitude > -11.10
                                                if month <= 6.00:
                                                    return 'Cloudy'
                                                else:  # month > 6.00
                                                    return 'Storm'
                                    else:  # pres > 1016.15
                                        if latitude <= -28.71:
                                            if month <= 11.50:
                                                if temp <= 23.15:
                                                    return 'Rain'
                                                else:  # temp > 23.15
                                                    return 'Clear'
                                            else:  # month > 11.50
                                                if hour <= 21.50:
                                                    return 'Cloudy'
                                                else:  # hour > 21.50
                                                    return 'Rain'
                                        else:  # latitude > -28.71
                                            if pres <= 1017.95:
                                                if temp <= 21.05:
                                                    return 'Storm'
                                                else:  # temp > 21.05
                                                    return 'Rain'
                                            else:  # pres > 1017.95
                                                if temp <= 21.90:
                                                    return 'Rain'
                                                else:  # temp > 21.90
                                                    return 'Fog'
                        else:  # rhum > 97.50
                            if temp <= 19.05:
                                if rhum <= 98.50:
                                    if temp <= 16.65:
                                        if month <= 8.50:
                                            if month <= 4.50:
                                                if dew_point <= 15.38:
                                                    return 'Clear'
                                                else:  # dew_point > 15.38
                                                    return 'Fog'
                                            else:  # month > 4.50
                                                if temp <= 14.15:
                                                    return 'Fog'
                                                else:  # temp > 14.15
                                                    return 'Fog'
                                        else:  # month > 8.50
                                            if hour <= 8.50:
                                                if hour <= 2.50:
                                                    return 'Clear'
                                                else:  # hour > 2.50
                                                    return 'Fog'
                                            else:  # hour > 8.50
                                                if pres <= 1020.45:
                                                    return 'Fog'
                                                else:  # pres > 1020.45
                                                    return 'Cloudy'
                                    else:  # temp > 16.65
                                        if hour <= 8.50:
                                            if month <= 4.50:
                                                if pres <= 1012.75:
                                                    return 'Rain'
                                                else:  # pres > 1012.75
                                                    return 'Cloudy'
                                            else:  # month > 4.50
                                                if month <= 9.50:
                                                    return 'Fog'
                                                else:  # month > 9.50
                                                    return 'Cloudy'
                                        else:  # hour > 8.50
                                            if hour <= 21.00:
                                                if hour <= 9.50:
                                                    return 'Fog'
                                                else:  # hour > 9.50
                                                    return 'Fog'
                                            else:  # hour > 21.00
                                                if hour <= 22.50:
                                                    return 'Rain'
                                                else:  # hour > 22.50
                                                    return 'Cloudy'
                                else:  # rhum > 98.50
                                    if month <= 2.50:
                                        if dew_point <= 17.37:
                                            if hour <= 8.50:
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Cloudy'
                                            else:  # hour > 8.50
                                                if rhum <= 99.50:
                                                    return 'Fog'
                                                else:  # rhum > 99.50
                                                    return 'Clear'
                                        else:  # dew_point > 17.37
                                            if hour <= 2.50:
                                                if dew_point <= 18.77:
                                                    return 'Rain'
                                                else:  # dew_point > 18.77
                                                    return 'Clear'
                                            else:  # hour > 2.50
                                                if pres <= 1011.85:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.85
                                                    return 'Fog'
                                    else:  # month > 2.50
                                        if pres <= 1015.15:
                                            if month <= 6.50:
                                                if pres <= 1014.25:
                                                    return 'Rain'
                                                else:  # pres > 1014.25
                                                    return 'Fog'
                                            else:  # month > 6.50
                                                if temp <= 17.75:
                                                    return 'Fog'
                                                else:  # temp > 17.75
                                                    return 'Fog'
                                        else:  # pres > 1015.15
                                            if month <= 11.50:
                                                if hour <= 1.50:
                                                    return 'Fog'
                                                else:  # hour > 1.50
                                                    return 'Fog'
                                            else:  # month > 11.50
                                                if temp <= 17.55:
                                                    return 'Fog'
                                                else:  # temp > 17.55
                                                    return 'Rain'
                            else:  # temp > 19.05
                                if hour <= 4.50:
                                    if pres <= 1017.35:
                                        if dew_point <= 19.49:
                                            if rhum <= 98.50:
                                                if temp <= 19.75:
                                                    return 'Rain'
                                                else:  # temp > 19.75
                                                    return 'Fog'
                                            else:  # rhum > 98.50
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Fog'
                                        else:  # dew_point > 19.49
                                            if month <= 2.50:
                                                if pres <= 1015.05:
                                                    return 'Clear'
                                                else:  # pres > 1015.05
                                                    return 'Clear'
                                            else:  # month > 2.50
                                                if dew_point <= 21.09:
                                                    return 'Rain'
                                                else:  # dew_point > 21.09
                                                    return 'Clear'
                                    else:  # pres > 1017.35
                                        if month <= 1.50:
                                            if temp <= 20.05:
                                                return 'Clear'
                                            else:  # temp > 20.05
                                                if dew_point <= 20.04:
                                                    return 'Cloudy'
                                                else:  # dew_point > 20.04
                                                    return 'Cloudy'
                                        else:  # month > 1.50
                                            if pres <= 1021.80:
                                                if dew_point <= 20.29:
                                                    return 'Cloudy'
                                                else:  # dew_point > 20.29
                                                    return 'Rain'
                                            else:  # pres > 1021.80
                                                return 'Rain'
                                else:  # hour > 4.50
                                    if dew_point <= 20.99:
                                        if pres <= 1012.25:
                                            if dew_point <= 20.19:
                                                if month <= 6.50:
                                                    return 'Rain'
                                                else:  # month > 6.50
                                                    return 'Rain'
                                            else:  # dew_point > 20.19
                                                return 'Fog'
                                        else:  # pres > 1012.25
                                            if month <= 7.50:
                                                if temp <= 20.05:
                                                    return 'Rain'
                                                else:  # temp > 20.05
                                                    return 'Fog'
                                            else:  # month > 7.50
                                                if dew_point <= 19.01:
                                                    return 'Cloudy'
                                                else:  # dew_point > 19.01
                                                    return 'Fog'
                                    else:  # dew_point > 20.99
                                        if hour <= 20.00:
                                            if hour <= 14.00:
                                                if temp <= 21.20:
                                                    return 'Rain'
                                                else:  # temp > 21.20
                                                    return 'Rain'
                                            else:  # hour > 14.00
                                                return 'Storm'
                                        else:  # hour > 20.00
                                            if temp <= 21.45:
                                                return 'Rain'
                                            else:  # temp > 21.45
                                                return 'Fog'
                    else:  # latitude > 15.70
                        if rhum <= 86.50:
                            if latitude <= 31.28:
                                if pres <= 1013.75:
                                    if hour <= 2.50:
                                        if month <= 2.50:
                                            if month <= 1.50:
                                                return 'Clear'
                                            else:  # month > 1.50
                                                if pres <= 1013.25:
                                                    return 'Fog'
                                                else:  # pres > 1013.25
                                                    return 'Cloudy'
                                        else:  # month > 2.50
                                            if dew_point <= 18.98:
                                                if month <= 10.50:
                                                    return 'Clear'
                                                else:  # month > 10.50
                                                    return 'Fog'
                                            else:  # dew_point > 18.98
                                                if dew_point <= 19.96:
                                                    return 'Fog'
                                                else:  # dew_point > 19.96
                                                    return 'Clear'
                                    else:  # hour > 2.50
                                        if hour <= 8.50:
                                            if month <= 6.50:
                                                if dew_point <= 18.95:
                                                    return 'Clear'
                                                else:  # dew_point > 18.95
                                                    return 'Fog'
                                            else:  # month > 6.50
                                                if pres <= 1009.95:
                                                    return 'Fog'
                                                else:  # pres > 1009.95
                                                    return 'Fog'
                                        else:  # hour > 8.50
                                            if hour <= 18.50:
                                                if dew_point <= 13.03:
                                                    return 'Rain'
                                                else:  # dew_point > 13.03
                                                    return 'Cloudy'
                                            else:  # hour > 18.50
                                                if month <= 10.50:
                                                    return 'Clear'
                                                else:  # month > 10.50
                                                    return 'Rain'
                                else:  # pres > 1013.75
                                    if hour <= 19.50:
                                        if hour <= 4.50:
                                            if month <= 10.50:
                                                if month <= 3.50:
                                                    return 'Fog'
                                                else:  # month > 3.50
                                                    return 'Fog'
                                            else:  # month > 10.50
                                                if pres <= 1023.25:
                                                    return 'Fog'
                                                else:  # pres > 1023.25
                                                    return 'Clear'
                                        else:  # hour > 4.50
                                            if rhum <= 78.50:
                                                if hour <= 18.50:
                                                    return 'Fog'
                                                else:  # hour > 18.50
                                                    return 'Fog'
                                            else:  # rhum > 78.50
                                                if pres <= 1013.85:
                                                    return 'Cloudy'
                                                else:  # pres > 1013.85
                                                    return 'Fog'
                                    else:  # hour > 19.50
                                        if dew_point <= 17.22:
                                            if pres <= 1014.75:
                                                if temp <= 13.50:
                                                    return 'Rain'
                                                else:  # temp > 13.50
                                                    return 'Clear'
                                            else:  # pres > 1014.75
                                                if pres <= 1023.10:
                                                    return 'Fog'
                                                else:  # pres > 1023.10
                                                    return 'Clear'
                                        else:  # dew_point > 17.22
                                            if pres <= 1014.05:
                                                if month <= 10.50:
                                                    return 'Fog'
                                                else:  # month > 10.50
                                                    return 'Clear'
                                            else:  # pres > 1014.05
                                                if hour <= 20.50:
                                                    return 'Clear'
                                                else:  # hour > 20.50
                                                    return 'Clear'
                            else:  # latitude > 31.28
                                if month <= 8.50:
                                    if hour <= 12.50:
                                        if month <= 2.50:
                                            if pres <= 1014.25:
                                                if rhum <= 76.50:
                                                    return 'Fog'
                                                else:  # rhum > 76.50
                                                    return 'Rain'
                                            else:  # pres > 1014.25
                                                if pres <= 1020.45:
                                                    return 'Fog'
                                                else:  # pres > 1020.45
                                                    return 'Fog'
                                        else:  # month > 2.50
                                            if rhum <= 82.50:
                                                if hour <= 2.50:
                                                    return 'Fog'
                                                else:  # hour > 2.50
                                                    return 'Cloudy'
                                            else:  # rhum > 82.50
                                                if month <= 4.50:
                                                    return 'Fog'
                                                else:  # month > 4.50
                                                    return 'Fog'
                                    else:  # hour > 12.50
                                        if hour <= 16.50:
                                            if rhum <= 81.50:
                                                if dew_point <= 17.49:
                                                    return 'Fog'
                                                else:  # dew_point > 17.49
                                                    return 'Cloudy'
                                            else:  # rhum > 81.50
                                                if temp <= 14.50:
                                                    return 'Fog'
                                                else:  # temp > 14.50
                                                    return 'Fog'
                                        else:  # hour > 16.50
                                            if temp <= 13.95:
                                                if pres <= 1014.85:
                                                    return 'Rain'
                                                else:  # pres > 1014.85
                                                    return 'Fog'
                                            else:  # temp > 13.95
                                                if pres <= 1020.45:
                                                    return 'Fog'
                                                else:  # pres > 1020.45
                                                    return 'Cloudy'
                                else:  # month > 8.50
                                    if pres <= 1015.45:
                                        if month <= 11.50:
                                            if rhum <= 79.50:
                                                if hour <= 13.50:
                                                    return 'Fog'
                                                else:  # hour > 13.50
                                                    return 'Fog'
                                            else:  # rhum > 79.50
                                                if hour <= 9.50:
                                                    return 'Fog'
                                                else:  # hour > 9.50
                                                    return 'Fog'
                                        else:  # month > 11.50
                                            if temp <= 9.70:
                                                if dew_point <= 4.15:
                                                    return 'Clear'
                                                else:  # dew_point > 4.15
                                                    return 'Fog'
                                            else:  # temp > 9.70
                                                if pres <= 1015.15:
                                                    return 'Rain'
                                                else:  # pres > 1015.15
                                                    return 'Fog'
                                    else:  # pres > 1015.45
                                        if hour <= 6.50:
                                            if month <= 10.50:
                                                if hour <= 4.50:
                                                    return 'Clear'
                                                else:  # hour > 4.50
                                                    return 'Fog'
                                            else:  # month > 10.50
                                                if dew_point <= 8.30:
                                                    return 'Clear'
                                                else:  # dew_point > 8.30
                                                    return 'Fog'
                                        else:  # hour > 6.50
                                            if dew_point <= 7.23:
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Fog'
                                            else:  # dew_point > 7.23
                                                if temp <= 19.35:
                                                    return 'Fog'
                                                else:  # temp > 19.35
                                                    return 'Fog'
                        else:  # rhum > 86.50
                            if rhum <= 92.50:
                                if pres <= 1002.20:
                                    return 'Rain'
                                else:  # pres > 1002.20
                                    if latitude <= 31.28:
                                        if pres <= 1010.50:
                                            if dew_point <= 19.43:
                                                if hour <= 6.50:
                                                    return 'Clear'
                                                else:  # hour > 6.50
                                                    return 'Fog'
                                            else:  # dew_point > 19.43
                                                if month <= 5.50:
                                                    return 'Fog'
                                                else:  # month > 5.50
                                                    return 'Fog'
                                        else:  # pres > 1010.50
                                            if dew_point <= 21.49:
                                                if rhum <= 89.50:
                                                    return 'Fog'
                                                else:  # rhum > 89.50
                                                    return 'Fog'
                                            else:  # dew_point > 21.49
                                                return 'Clear'
                                    else:  # latitude > 31.28
                                        if hour <= 12.50:
                                            if month <= 10.50:
                                                if rhum <= 89.50:
                                                    return 'Fog'
                                                else:  # rhum > 89.50
                                                    return 'Fog'
                                            else:  # month > 10.50
                                                if dew_point <= 8.57:
                                                    return 'Fog'
                                                else:  # dew_point > 8.57
                                                    return 'Fog'
                                        else:  # hour > 12.50
                                            if hour <= 19.50:
                                                if month <= 4.50:
                                                    return 'Fog'
                                                else:  # month > 4.50
                                                    return 'Fog'
                                            else:  # hour > 19.50
                                                if pres <= 1017.15:
                                                    return 'Rain'
                                                else:  # pres > 1017.15
                                                    return 'Fog'
                            else:  # rhum > 92.50
                                if pres <= 1002.40:
                                    if hour <= 16.50:
                                        if dew_point <= 12.52:
                                            return 'Rain'
                                        else:  # dew_point > 12.52
                                            return 'Rain'
                                    else:  # hour > 16.50
                                        if hour <= 19.00:
                                            return 'Cloudy'
                                        else:  # hour > 19.00
                                            return 'Rain'
                                else:  # pres > 1002.40
                                    if dew_point <= 19.70:
                                        if pres <= 1006.05:
                                            if hour <= 6.50:
                                                return 'Cloudy'
                                            else:  # hour > 6.50
                                                return 'Rain'
                                        else:  # pres > 1006.05
                                            if rhum <= 95.50:
                                                if latitude <= 31.28:
                                                    return 'Fog'
                                                else:  # latitude > 31.28
                                                    return 'Fog'
                                            else:  # rhum > 95.50
                                                if pres <= 1013.15:
                                                    return 'Fog'
                                                else:  # pres > 1013.15
                                                    return 'Fog'
                                    else:  # dew_point > 19.70
                                        if month <= 8.50:
                                            if hour <= 5.50:
                                                if pres <= 1014.90:
                                                    return 'Cloudy'
                                                else:  # pres > 1014.90
                                                    return 'Fog'
                                            else:  # hour > 5.50
                                                if hour <= 17.50:
                                                    return 'Fog'
                                                else:  # hour > 17.50
                                                    return 'Cloudy'
                                        else:  # month > 8.50
                                            if rhum <= 96.50:
                                                if month <= 10.50:
                                                    return 'Fog'
                                                else:  # month > 10.50
                                                    return 'Fog'
                                            else:  # rhum > 96.50
                                                if pres <= 1016.65:
                                                    return 'Fog'
                                                else:  # pres > 1016.65
                                                    return 'Cloudy'
                else:  # latitude > 34.10
                    if pres <= 1013.35:
                        if rhum <= 86.50:
                            if temp <= 16.55:
                                if pres <= 1004.55:
                                    if temp <= 4.55:
                                        if latitude <= 50.40:
                                            if month <= 1.50:
                                                if temp <= 4.05:
                                                    return 'Snow'
                                                else:  # temp > 4.05
                                                    return 'Rain'
                                            else:  # month > 1.50
                                                if dew_point <= 0.76:
                                                    return 'Cloudy'
                                                else:  # dew_point > 0.76
                                                    return 'Rain'
                                        else:  # latitude > 50.40
                                            if latitude <= 53.63:
                                                if month <= 11.50:
                                                    return 'Clear'
                                                else:  # month > 11.50
                                                    return 'Cloudy'
                                            else:  # latitude > 53.63
                                                if pres <= 994.05:
                                                    return 'Rain'
                                                else:  # pres > 994.05
                                                    return 'Rain'
                                    else:  # temp > 4.55
                                        if latitude <= 59.95:
                                            if latitude <= 42.48:
                                                if dew_point <= 9.08:
                                                    return 'Clear'
                                                else:  # dew_point > 9.08
                                                    return 'Rain'
                                            else:  # latitude > 42.48
                                                if pres <= 993.05:
                                                    return 'Rain'
                                                else:  # pres > 993.05
                                                    return 'Rain'
                                        else:  # latitude > 59.95
                                            if month <= 5.50:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Rain'
                                            else:  # month > 5.50
                                                if rhum <= 80.50:
                                                    return 'Rain'
                                                else:  # rhum > 80.50
                                                    return 'Rain'
                                else:  # pres > 1004.55
                                    if latitude <= 42.48:
                                        if hour <= 8.50:
                                            if pres <= 1009.30:
                                                if month <= 4.50:
                                                    return 'Rain'
                                                else:  # month > 4.50
                                                    return 'Clear'
                                            else:  # pres > 1009.30
                                                if dew_point <= 7.32:
                                                    return 'Rain'
                                                else:  # dew_point > 7.32
                                                    return 'Rain'
                                        else:  # hour > 8.50
                                            if pres <= 1011.45:
                                                if pres <= 1008.00:
                                                    return 'Clear'
                                                else:  # pres > 1008.00
                                                    return 'Clear'
                                            else:  # pres > 1011.45
                                                if pres <= 1012.75:
                                                    return 'Clear'
                                                else:  # pres > 1012.75
                                                    return 'Clear'
                                    else:  # latitude > 42.48
                                        if dew_point <= 0.86:
                                            if pres <= 1008.85:
                                                if pres <= 1005.35:
                                                    return 'Cloudy'
                                                else:  # pres > 1005.35
                                                    return 'Snow'
                                            else:  # pres > 1008.85
                                                if latitude <= 53.63:
                                                    return 'Clear'
                                                else:  # latitude > 53.63
                                                    return 'Cloudy'
                                        else:  # dew_point > 0.86
                                            if month <= 5.50:
                                                if latitude <= 59.95:
                                                    return 'Rain'
                                                else:  # latitude > 59.95
                                                    return 'Rain'
                                            else:  # month > 5.50
                                                if latitude <= 59.95:
                                                    return 'Cloudy'
                                                else:  # latitude > 59.95
                                                    return 'Cloudy'
                            else:  # temp > 16.55
                                if latitude <= 53.63:
                                    if latitude <= 50.40:
                                        if latitude <= 42.48:
                                            if hour <= 8.50:
                                                if rhum <= 79.50:
                                                    return 'Rain'
                                                else:  # rhum > 79.50
                                                    return 'Rain'
                                            else:  # hour > 8.50
                                                if dew_point <= 21.79:
                                                    return 'Clear'
                                                else:  # dew_point > 21.79
                                                    return 'Rain'
                                        else:  # latitude > 42.48
                                            if temp <= 21.45:
                                                if hour <= 15.50:
                                                    return 'Clear'
                                                else:  # hour > 15.50
                                                    return 'Cloudy'
                                            else:  # temp > 21.45
                                                if dew_point <= 16.93:
                                                    return 'Storm'
                                                else:  # dew_point > 16.93
                                                    return 'Clear'
                                    else:  # latitude > 50.40
                                        if hour <= 8.50:
                                            if pres <= 998.55:
                                                return 'Rain'
                                            else:  # pres > 998.55
                                                if rhum <= 83.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 83.50
                                                    return 'Cloudy'
                                        else:  # hour > 8.50
                                            if hour <= 19.50:
                                                if pres <= 1011.75:
                                                    return 'Rain'
                                                else:  # pres > 1011.75
                                                    return 'Rain'
                                            else:  # hour > 19.50
                                                if month <= 9.50:
                                                    return 'Cloudy'
                                                else:  # month > 9.50
                                                    return 'Rain'
                                else:  # latitude > 53.63
                                    if hour <= 10.50:
                                        if hour <= 6.50:
                                            if hour <= 4.50:
                                                if temp <= 20.70:
                                                    return 'Cloudy'
                                                else:  # temp > 20.70
                                                    return 'Clear'
                                            else:  # hour > 4.50
                                                if dew_point <= 18.28:
                                                    return 'Cloudy'
                                                else:  # dew_point > 18.28
                                                    return 'Rain'
                                        else:  # hour > 6.50
                                            if rhum <= 75.50:
                                                return 'Cloudy'
                                            else:  # rhum > 75.50
                                                if pres <= 1007.15:
                                                    return 'Rain'
                                                else:  # pres > 1007.15
                                                    return 'Rain'
                                    else:  # hour > 10.50
                                        if hour <= 18.50:
                                            if pres <= 1004.05:
                                                if dew_point <= 13.32:
                                                    return 'Rain'
                                                else:  # dew_point > 13.32
                                                    return 'Storm'
                                            else:  # pres > 1004.05
                                                if pres <= 1007.80:
                                                    return 'Rain'
                                                else:  # pres > 1007.80
                                                    return 'Storm'
                                        else:  # hour > 18.50
                                            if pres <= 1003.20:
                                                if hour <= 20.50:
                                                    return 'Rain'
                                                else:  # hour > 20.50
                                                    return 'Clear'
                                            else:  # pres > 1003.20
                                                if dew_point <= 13.65:
                                                    return 'Clear'
                                                else:  # dew_point > 13.65
                                                    return 'Cloudy'
                        else:  # rhum > 86.50
                            if latitude <= 42.48:
                                if rhum <= 92.50:
                                    if hour <= 10.50:
                                        if month <= 9.50:
                                            if hour <= 0.50:
                                                if pres <= 1006.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1006.95
                                                    return 'Rain'
                                            else:  # hour > 0.50
                                                if hour <= 9.50:
                                                    return 'Rain'
                                                else:  # hour > 9.50
                                                    return 'Rain'
                                        else:  # month > 9.50
                                            if hour <= 0.50:
                                                if pres <= 1011.85:
                                                    return 'Rain'
                                                else:  # pres > 1011.85
                                                    return 'Rain'
                                            else:  # hour > 0.50
                                                if temp <= 20.05:
                                                    return 'Rain'
                                                else:  # temp > 20.05
                                                    return 'Clear'
                                    else:  # hour > 10.50
                                        if rhum <= 90.50:
                                            if hour <= 21.50:
                                                if month <= 10.50:
                                                    return 'Clear'
                                                else:  # month > 10.50
                                                    return 'Clear'
                                            else:  # hour > 21.50
                                                if dew_point <= 20.86:
                                                    return 'Rain'
                                                else:  # dew_point > 20.86
                                                    return 'Cloudy'
                                        else:  # rhum > 90.50
                                            if pres <= 998.20:
                                                if hour <= 17.50:
                                                    return 'Rain'
                                                else:  # hour > 17.50
                                                    return 'Rain'
                                            else:  # pres > 998.20
                                                if hour <= 21.50:
                                                    return 'Rain'
                                                else:  # hour > 21.50
                                                    return 'Rain'
                                else:  # rhum > 92.50
                                    if hour <= 11.50:
                                        if hour <= 9.50:
                                            if pres <= 1013.25:
                                                if rhum <= 97.50:
                                                    return 'Rain'
                                                else:  # rhum > 97.50
                                                    return 'Rain'
                                            else:  # pres > 1013.25
                                                return 'Clear'
                                        else:  # hour > 9.50
                                            if month <= 11.50:
                                                if pres <= 990.25:
                                                    return 'Cloudy'
                                                else:  # pres > 990.25
                                                    return 'Rain'
                                            else:  # month > 11.50
                                                return 'Clear'
                                    else:  # hour > 11.50
                                        if rhum <= 96.50:
                                            if hour <= 21.50:
                                                if pres <= 1003.95:
                                                    return 'Rain'
                                                else:  # pres > 1003.95
                                                    return 'Rain'
                                            else:  # hour > 21.50
                                                if dew_point <= 17.07:
                                                    return 'Rain'
                                                else:  # dew_point > 17.07
                                                    return 'Rain'
                                        else:  # rhum > 96.50
                                            if dew_point <= 16.89:
                                                if dew_point <= 14.47:
                                                    return 'Rain'
                                                else:  # dew_point > 14.47
                                                    return 'Rain'
                                            else:  # dew_point > 16.89
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Rain'
                            else:  # latitude > 42.48
                                if temp <= 18.25:
                                    if pres <= 1007.75:
                                        if temp <= 3.35:
                                            if latitude <= 50.40:
                                                if hour <= 14.00:
                                                    return 'Rain'
                                                else:  # hour > 14.00
                                                    return 'Snow'
                                            else:  # latitude > 50.40
                                                if dew_point <= 1.51:
                                                    return 'Snow'
                                                else:  # dew_point > 1.51
                                                    return 'Rain'
                                        else:  # temp > 3.35
                                            if rhum <= 99.50:
                                                if temp <= 14.05:
                                                    return 'Rain'
                                                else:  # temp > 14.05
                                                    return 'Rain'
                                            else:  # rhum > 99.50
                                                if hour <= 6.50:
                                                    return 'Fog'
                                                else:  # hour > 6.50
                                                    return 'Rain'
                                    else:  # pres > 1007.75
                                        if month <= 4.50:
                                            if dew_point <= 3.51:
                                                if latitude <= 50.40:
                                                    return 'Snow'
                                                else:  # latitude > 50.40
                                                    return 'Rain'
                                            else:  # dew_point > 3.51
                                                if dew_point <= 5.94:
                                                    return 'Rain'
                                                else:  # dew_point > 5.94
                                                    return 'Rain'
                                        else:  # month > 4.50
                                            if rhum <= 98.50:
                                                if temp <= 4.75:
                                                    return 'Snow'
                                                else:  # temp > 4.75
                                                    return 'Rain'
                                            else:  # rhum > 98.50
                                                if dew_point <= 9.68:
                                                    return 'Rain'
                                                else:  # dew_point > 9.68
                                                    return 'Fog'
                                else:  # temp > 18.25
                                    if month <= 7.50:
                                        if hour <= 11.50:
                                            if pres <= 1007.25:
                                                if dew_point <= 18.02:
                                                    return 'Cloudy'
                                                else:  # dew_point > 18.02
                                                    return 'Rain'
                                            else:  # pres > 1007.25
                                                if month <= 6.50:
                                                    return 'Rain'
                                                else:  # month > 6.50
                                                    return 'Clear'
                                        else:  # hour > 11.50
                                            if hour <= 18.50:
                                                if pres <= 1011.85:
                                                    return 'Storm'
                                                else:  # pres > 1011.85
                                                    return 'Fog'
                                            else:  # hour > 18.50
                                                if pres <= 1004.10:
                                                    return 'Cloudy'
                                                else:  # pres > 1004.10
                                                    return 'Clear'
                                    else:  # month > 7.50
                                        if pres <= 1009.25:
                                            if latitude <= 53.63:
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Cloudy'
                                            else:  # latitude > 53.63
                                                if rhum <= 96.50:
                                                    return 'Rain'
                                                else:  # rhum > 96.50
                                                    return 'Cloudy'
                                        else:  # pres > 1009.25
                                            if dew_point <= 17.41:
                                                if temp <= 18.65:
                                                    return 'Rain'
                                                else:  # temp > 18.65
                                                    return 'Cloudy'
                                            else:  # dew_point > 17.41
                                                if temp <= 18.75:
                                                    return 'Rain'
                                                else:  # temp > 18.75
                                                    return 'Rain'
                    else:  # pres > 1013.35
                        if latitude <= 42.48:
                            if rhum <= 92.50:
                                if hour <= 10.50:
                                    if rhum <= 86.50:
                                        if month <= 9.50:
                                            if month <= 6.50:
                                                if dew_point <= 17.95:
                                                    return 'Rain'
                                                else:  # dew_point > 17.95
                                                    return 'Clear'
                                            else:  # month > 6.50
                                                if temp <= 24.75:
                                                    return 'Rain'
                                                else:  # temp > 24.75
                                                    return 'Clear'
                                        else:  # month > 9.50
                                            if temp <= 18.95:
                                                if hour <= 7.50:
                                                    return 'Rain'
                                                else:  # hour > 7.50
                                                    return 'Clear'
                                            else:  # temp > 18.95
                                                if rhum <= 81.50:
                                                    return 'Clear'
                                                else:  # rhum > 81.50
                                                    return 'Clear'
                                    else:  # rhum > 86.50
                                        if temp <= 3.65:
                                            return 'Snow'
                                        else:  # temp > 3.65
                                            if month <= 9.50:
                                                if dew_point <= 8.05:
                                                    return 'Rain'
                                                else:  # dew_point > 8.05
                                                    return 'Rain'
                                            else:  # month > 9.50
                                                if temp <= 18.55:
                                                    return 'Rain'
                                                else:  # temp > 18.55
                                                    return 'Clear'
                                else:  # hour > 10.50
                                    if rhum <= 85.50:
                                        if month <= 3.50:
                                            if dew_point <= 4.49:
                                                if rhum <= 83.50:
                                                    return 'Clear'
                                                else:  # rhum > 83.50
                                                    return 'Rain'
                                            else:  # dew_point > 4.49
                                                if pres <= 1018.15:
                                                    return 'Rain'
                                                else:  # pres > 1018.15
                                                    return 'Clear'
                                        else:  # month > 3.50
                                            if dew_point <= 9.43:
                                                if pres <= 1018.25:
                                                    return 'Clear'
                                                else:  # pres > 1018.25
                                                    return 'Clear'
                                            else:  # dew_point > 9.43
                                                if dew_point <= 15.86:
                                                    return 'Clear'
                                                else:  # dew_point > 15.86
                                                    return 'Clear'
                                    else:  # rhum > 85.50
                                        if temp <= 3.15:
                                            return 'Snow'
                                        else:  # temp > 3.15
                                            if month <= 7.50:
                                                if dew_point <= 7.51:
                                                    return 'Rain'
                                                else:  # dew_point > 7.51
                                                    return 'Clear'
                                            else:  # month > 7.50
                                                if pres <= 1014.25:
                                                    return 'Rain'
                                                else:  # pres > 1014.25
                                                    return 'Clear'
                            else:  # rhum > 92.50
                                if hour <= 12.50:
                                    if dew_point <= 2.57:
                                        if rhum <= 94.00:
                                            return 'Rain'
                                        else:  # rhum > 94.00
                                            return 'Snow'
                                    else:  # dew_point > 2.57
                                        if month <= 10.50:
                                            if dew_point <= 3.02:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 3.02
                                                if dew_point <= 21.47:
                                                    return 'Rain'
                                                else:  # dew_point > 21.47
                                                    return 'Rain'
                                        else:  # month > 10.50
                                            if rhum <= 94.50:
                                                if pres <= 1020.05:
                                                    return 'Rain'
                                                else:  # pres > 1020.05
                                                    return 'Clear'
                                            else:  # rhum > 94.50
                                                if pres <= 1023.10:
                                                    return 'Rain'
                                                else:  # pres > 1023.10
                                                    return 'Rain'
                                else:  # hour > 12.50
                                    if rhum <= 96.50:
                                        if month <= 9.50:
                                            if temp <= 21.35:
                                                if pres <= 1025.05:
                                                    return 'Rain'
                                                else:  # pres > 1025.05
                                                    return 'Clear'
                                            else:  # temp > 21.35
                                                if hour <= 20.50:
                                                    return 'Clear'
                                                else:  # hour > 20.50
                                                    return 'Rain'
                                        else:  # month > 9.50
                                            if dew_point <= 6.50:
                                                return 'Clear'
                                            else:  # dew_point > 6.50
                                                if dew_point <= 17.90:
                                                    return 'Rain'
                                                else:  # dew_point > 17.90
                                                    return 'Clear'
                                    else:  # rhum > 96.50
                                        if temp <= 18.55:
                                            if rhum <= 99.50:
                                                if temp <= 12.75:
                                                    return 'Rain'
                                                else:  # temp > 12.75
                                                    return 'Rain'
                                            else:  # rhum > 99.50
                                                if temp <= 10.45:
                                                    return 'Clear'
                                                else:  # temp > 10.45
                                                    return 'Rain'
                                        else:  # temp > 18.55
                                            if rhum <= 97.50:
                                                if pres <= 1015.90:
                                                    return 'Rain'
                                                else:  # pres > 1015.90
                                                    return 'Clear'
                                            else:  # rhum > 97.50
                                                if pres <= 1018.25:
                                                    return 'Rain'
                                                else:  # pres > 1018.25
                                                    return 'Clear'
                        else:  # latitude > 42.48
                            if rhum <= 92.50:
                                if latitude <= 59.95:
                                    if latitude <= 50.40:
                                        if month <= 9.50:
                                            if month <= 6.50:
                                                if rhum <= 87.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 87.50
                                                    return 'Cloudy'
                                            else:  # month > 6.50
                                                if hour <= 16.50:
                                                    return 'Clear'
                                                else:  # hour > 16.50
                                                    return 'Cloudy'
                                        else:  # month > 9.50
                                            if dew_point <= 10.19:
                                                if dew_point <= 4.55:
                                                    return 'Cloudy'
                                                else:  # dew_point > 4.55
                                                    return 'Cloudy'
                                            else:  # dew_point > 10.19
                                                if pres <= 1016.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1016.95
                                                    return 'Fog'
                                    else:  # latitude > 50.40
                                        if temp <= 17.35:
                                            if pres <= 1017.35:
                                                if dew_point <= 1.36:
                                                    return 'Snow'
                                                else:  # dew_point > 1.36
                                                    return 'Cloudy'
                                            else:  # pres > 1017.35
                                                if month <= 9.50:
                                                    return 'Cloudy'
                                                else:  # month > 9.50
                                                    return 'Cloudy'
                                        else:  # temp > 17.35
                                            if latitude <= 53.63:
                                                if pres <= 1017.45:
                                                    return 'Cloudy'
                                                else:  # pres > 1017.45
                                                    return 'Cloudy'
                                            else:  # latitude > 53.63
                                                if hour <= 10.50:
                                                    return 'Clear'
                                                else:  # hour > 10.50
                                                    return 'Storm'
                                else:  # latitude > 59.95
                                    if month <= 5.50:
                                        if pres <= 1025.95:
                                            if dew_point <= 3.53:
                                                if pres <= 1020.25:
                                                    return 'Rain'
                                                else:  # pres > 1020.25
                                                    return 'Cloudy'
                                            else:  # dew_point > 3.53
                                                if dew_point <= 6.93:
                                                    return 'Rain'
                                                else:  # dew_point > 6.93
                                                    return 'Rain'
                                        else:  # pres > 1025.95
                                            if dew_point <= 4.99:
                                                if month <= 3.50:
                                                    return 'Cloudy'
                                                else:  # month > 3.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 4.99
                                                if hour <= 13.50:
                                                    return 'Rain'
                                                else:  # hour > 13.50
                                                    return 'Fog'
                                    else:  # month > 5.50
                                        if month <= 7.50:
                                            if month <= 6.50:
                                                if rhum <= 83.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 83.50
                                                    return 'Rain'
                                            else:  # month > 6.50
                                                if rhum <= 77.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 77.50
                                                    return 'Fog'
                                        else:  # month > 7.50
                                            if pres <= 1023.45:
                                                if rhum <= 81.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 81.50
                                                    return 'Rain'
                                            else:  # pres > 1023.45
                                                if dew_point <= 6.94:
                                                    return 'Cloudy'
                                                else:  # dew_point > 6.94
                                                    return 'Cloudy'
                            else:  # rhum > 92.50
                                if rhum <= 98.50:
                                    if pres <= 1019.15:
                                        if temp <= 8.85:
                                            if dew_point <= 2.95:
                                                if latitude <= 50.40:
                                                    return 'Snow'
                                                else:  # latitude > 50.40
                                                    return 'Rain'
                                            else:  # dew_point > 2.95
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Rain'
                                        else:  # temp > 8.85
                                            if month <= 9.50:
                                                if latitude <= 59.95:
                                                    return 'Rain'
                                                else:  # latitude > 59.95
                                                    return 'Fog'
                                            else:  # month > 9.50
                                                if latitude <= 50.40:
                                                    return 'Fog'
                                                else:  # latitude > 50.40
                                                    return 'Rain'
                                    else:  # pres > 1019.15
                                        if latitude <= 50.40:
                                            if temp <= 11.25:
                                                if dew_point <= 6.38:
                                                    return 'Fog'
                                                else:  # dew_point > 6.38
                                                    return 'Rain'
                                            else:  # temp > 11.25
                                                if temp <= 14.65:
                                                    return 'Fog'
                                                else:  # temp > 14.65
                                                    return 'Cloudy'
                                        else:  # latitude > 50.40
                                            if latitude <= 59.95:
                                                if pres <= 1026.05:
                                                    return 'Cloudy'
                                                else:  # pres > 1026.05
                                                    return 'Cloudy'
                                            else:  # latitude > 59.95
                                                if dew_point <= 9.90:
                                                    return 'Fog'
                                                else:  # dew_point > 9.90
                                                    return 'Rain'
                                else:  # rhum > 98.50
                                    if month <= 9.50:
                                        if pres <= 1031.65:
                                            if month <= 6.50:
                                                if hour <= 9.50:
                                                    return 'Rain'
                                                else:  # hour > 9.50
                                                    return 'Rain'
                                            else:  # month > 6.50
                                                if latitude <= 59.95:
                                                    return 'Clear'
                                                else:  # latitude > 59.95
                                                    return 'Fog'
                                        else:  # pres > 1031.65
                                            if dew_point <= 6.28:
                                                if hour <= 16.50:
                                                    return 'Fog'
                                                else:  # hour > 16.50
                                                    return 'Fog'
                                            else:  # dew_point > 6.28
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Fog'
                                    else:  # month > 9.50
                                        if latitude <= 50.40:
                                            if dew_point <= 11.60:
                                                if dew_point <= 5.63:
                                                    return 'Fog'
                                                else:  # dew_point > 5.63
                                                    return 'Rain'
                                            else:  # dew_point > 11.60
                                                if hour <= 4.50:
                                                    return 'Rain'
                                                else:  # hour > 4.50
                                                    return 'Fog'
                                        else:  # latitude > 50.40
                                            if pres <= 1038.75:
                                                if latitude <= 53.63:
                                                    return 'Fog'
                                                else:  # latitude > 53.63
                                                    return 'Cloudy'
                                            else:  # pres > 1038.75
                                                if latitude <= 53.63:
                                                    return 'Cloudy'
                                                else:  # latitude > 53.63
                                                    return 'Clear'
        else:  # dew_point > 21.83
            if hour <= 13.50:
                if hour <= 5.50:
                    if latitude <= 15.70:
                        if hour <= 4.50:
                            if rhum <= 83.50:
                                if month <= 4.50:
                                    if temp <= 32.50:
                                        if hour <= 3.50:
                                            if latitude <= -11.10:
                                                if temp <= 27.60:
                                                    return 'Rain'
                                                else:  # temp > 27.60
                                                    return 'Clear'
                                            else:  # latitude > -11.10
                                                if month <= 1.50:
                                                    return 'Cloudy'
                                                else:  # month > 1.50
                                                    return 'Cloudy'
                                        else:  # hour > 3.50
                                            if rhum <= 72.50:
                                                if month <= 2.50:
                                                    return 'Cloudy'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                            else:  # rhum > 72.50
                                                if dew_point <= 22.99:
                                                    return 'Rain'
                                                else:  # dew_point > 22.99
                                                    return 'Rain'
                                    else:  # temp > 32.50
                                        if pres <= 1010.50:
                                            if hour <= 2.00:
                                                return 'Clear'
                                            else:  # hour > 2.00
                                                if pres <= 1008.20:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.20
                                                    return 'Storm'
                                        else:  # pres > 1010.50
                                            if rhum <= 54.00:
                                                return 'Cloudy'
                                            else:  # rhum > 54.00
                                                if dew_point <= 23.49:
                                                    return 'Clear'
                                                else:  # dew_point > 23.49
                                                    return 'Cloudy'
                                else:  # month > 4.50
                                    if hour <= 1.50:
                                        if month <= 9.50:
                                            if month <= 8.50:
                                                if pres <= 1007.50:
                                                    return 'Fog'
                                                else:  # pres > 1007.50
                                                    return 'Rain'
                                            else:  # month > 8.50
                                                if dew_point <= 25.04:
                                                    return 'Rain'
                                                else:  # dew_point > 25.04
                                                    return 'Cloudy'
                                        else:  # month > 9.50
                                            if dew_point <= 25.04:
                                                if month <= 11.50:
                                                    return 'Rain'
                                                else:  # month > 11.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 25.04
                                                if pres <= 1009.50:
                                                    return 'Rain'
                                                else:  # pres > 1009.50
                                                    return 'Fog'
                                    else:  # hour > 1.50
                                        if temp <= 28.50:
                                            if month <= 11.50:
                                                if hour <= 3.50:
                                                    return 'Rain'
                                                else:  # hour > 3.50
                                                    return 'Rain'
                                            else:  # month > 11.50
                                                if hour <= 2.50:
                                                    return 'Cloudy'
                                                else:  # hour > 2.50
                                                    return 'Storm'
                                        else:  # temp > 28.50
                                            if temp <= 32.50:
                                                if rhum <= 57.50:
                                                    return 'Storm'
                                                else:  # rhum > 57.50
                                                    return 'Rain'
                                            else:  # temp > 32.50
                                                if rhum <= 61.50:
                                                    return 'Rain'
                                                else:  # rhum > 61.50
                                                    return 'Storm'
                            else:  # rhum > 83.50
                                if hour <= 1.50:
                                    if dew_point <= 25.50:
                                        if month <= 4.50:
                                            if temp <= 24.85:
                                                if rhum <= 90.00:
                                                    return 'Cloudy'
                                                else:  # rhum > 90.00
                                                    return 'Rain'
                                            else:  # temp > 24.85
                                                if dew_point <= 23.53:
                                                    return 'Cloudy'
                                                else:  # dew_point > 23.53
                                                    return 'Cloudy'
                                        else:  # month > 4.50
                                            if dew_point <= 24.05:
                                                if month <= 7.50:
                                                    return 'Storm'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                            else:  # dew_point > 24.05
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Fog'
                                    else:  # dew_point > 25.50
                                        if rhum <= 86.50:
                                            if month <= 6.50:
                                                if hour <= 0.50:
                                                    return 'Cloudy'
                                                else:  # hour > 0.50
                                                    return 'Rain'
                                            else:  # month > 6.50
                                                if pres <= 1012.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1012.50
                                                    return 'Fog'
                                        else:  # rhum > 86.50
                                            if month <= 9.50:
                                                if month <= 4.50:
                                                    return 'Fog'
                                                else:  # month > 4.50
                                                    return 'Fog'
                                            else:  # month > 9.50
                                                if pres <= 1010.50:
                                                    return 'Rain'
                                                else:  # pres > 1010.50
                                                    return 'Fog'
                                else:  # hour > 1.50
                                    if rhum <= 93.50:
                                        if pres <= 1012.40:
                                            if temp <= 25.30:
                                                if dew_point <= 23.00:
                                                    return 'Rain'
                                                else:  # dew_point > 23.00
                                                    return 'Storm'
                                            else:  # temp > 25.30
                                                if dew_point <= 26.51:
                                                    return 'Rain'
                                                else:  # dew_point > 26.51
                                                    return 'Rain'
                                        else:  # pres > 1012.40
                                            if hour <= 2.50:
                                                if dew_point <= 24.55:
                                                    return 'Rain'
                                                else:  # dew_point > 24.55
                                                    return 'Cloudy'
                                            else:  # hour > 2.50
                                                if month <= 3.50:
                                                    return 'Rain'
                                                else:  # month > 3.50
                                                    return 'Storm'
                                    else:  # rhum > 93.50
                                        if month <= 6.50:
                                            if pres <= 1013.50:
                                                if hour <= 3.50:
                                                    return 'Storm'
                                                else:  # hour > 3.50
                                                    return 'Rain'
                                            else:  # pres > 1013.50
                                                if month <= 5.50:
                                                    return 'Rain'
                                                else:  # month > 5.50
                                                    return 'Cloudy'
                                        else:  # month > 6.50
                                            if hour <= 3.50:
                                                if dew_point <= 25.48:
                                                    return 'Rain'
                                                else:  # dew_point > 25.48
                                                    return 'Cloudy'
                                            else:  # hour > 3.50
                                                if dew_point <= 24.48:
                                                    return 'Storm'
                                                else:  # dew_point > 24.48
                                                    return 'Rain'
                        else:  # hour > 4.50
                            if temp <= 30.50:
                                if month <= 11.50:
                                    if month <= 3.50:
                                        if pres <= 1010.90:
                                            if rhum <= 68.00:
                                                if month <= 1.50:
                                                    return 'Rain'
                                                else:  # month > 1.50
                                                    return 'Rain'
                                            else:  # rhum > 68.00
                                                if pres <= 1009.90:
                                                    return 'Rain'
                                                else:  # pres > 1009.90
                                                    return 'Rain'
                                        else:  # pres > 1010.90
                                            if temp <= 29.50:
                                                if dew_point <= 24.51:
                                                    return 'Rain'
                                                else:  # dew_point > 24.51
                                                    return 'Storm'
                                            else:  # temp > 29.50
                                                if month <= 1.50:
                                                    return 'Cloudy'
                                                else:  # month > 1.50
                                                    return 'Storm'
                                    else:  # month > 3.50
                                        if dew_point <= 23.98:
                                            if dew_point <= 22.52:
                                                if pres <= 1007.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1007.50
                                                    return 'Rain'
                                            else:  # dew_point > 22.52
                                                if month <= 4.50:
                                                    return 'Rain'
                                                else:  # month > 4.50
                                                    return 'Storm'
                                        else:  # dew_point > 23.98
                                            if month <= 6.50:
                                                if pres <= 1010.50:
                                                    return 'Storm'
                                                else:  # pres > 1010.50
                                                    return 'Rain'
                                            else:  # month > 6.50
                                                if temp <= 26.50:
                                                    return 'Rain'
                                                else:  # temp > 26.50
                                                    return 'Rain'
                                else:  # month > 11.50
                                    if pres <= 1010.50:
                                        if dew_point <= 21.97:
                                            if pres <= 1009.00:
                                                return 'Rain'
                                            else:  # pres > 1009.00
                                                return 'Rain'
                                        else:  # dew_point > 21.97
                                            if dew_point <= 23.49:
                                                return 'Rain'
                                            else:  # dew_point > 23.49
                                                if dew_point <= 23.91:
                                                    return 'Cloudy'
                                                else:  # dew_point > 23.91
                                                    return 'Rain'
                                    else:  # pres > 1010.50
                                        if dew_point <= 22.96:
                                            if dew_point <= 22.48:
                                                if pres <= 1011.50:
                                                    return 'Rain'
                                                else:  # pres > 1011.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 22.48
                                                return 'Cloudy'
                                        else:  # dew_point > 22.96
                                            if rhum <= 81.50:
                                                if temp <= 28.50:
                                                    return 'Cloudy'
                                                else:  # temp > 28.50
                                                    return 'Rain'
                                            else:  # rhum > 81.50
                                                return 'Rain'
                            else:  # temp > 30.50
                                if month <= 5.50:
                                    if rhum <= 59.50:
                                        if pres <= 1011.50:
                                            if month <= 3.50:
                                                if pres <= 1008.70:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.70
                                                    return 'Cloudy'
                                            else:  # month > 3.50
                                                if pres <= 1006.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1006.50
                                                    return 'Rain'
                                        else:  # pres > 1011.50
                                            return 'Cloudy'
                                    else:  # rhum > 59.50
                                        if rhum <= 64.50:
                                            if pres <= 1011.50:
                                                if month <= 3.50:
                                                    return 'Rain'
                                                else:  # month > 3.50
                                                    return 'Rain'
                                            else:  # pres > 1011.50
                                                if temp <= 31.50:
                                                    return 'Cloudy'
                                                else:  # temp > 31.50
                                                    return 'Cloudy'
                                        else:  # rhum > 64.50
                                            if month <= 2.50:
                                                if rhum <= 68.50:
                                                    return 'Rain'
                                                else:  # rhum > 68.50
                                                    return 'Cloudy'
                                            else:  # month > 2.50
                                                if temp <= 32.50:
                                                    return 'Rain'
                                                else:  # temp > 32.50
                                                    return 'Cloudy'
                                else:  # month > 5.50
                                    if dew_point <= 24.48:
                                        if month <= 11.50:
                                            if month <= 10.50:
                                                if pres <= 1008.50:
                                                    return 'Storm'
                                                else:  # pres > 1008.50
                                                    return 'Rain'
                                            else:  # month > 10.50
                                                if temp <= 32.50:
                                                    return 'Storm'
                                                else:  # temp > 32.50
                                                    return 'Rain'
                                        else:  # month > 11.50
                                            if pres <= 1010.50:
                                                if rhum <= 57.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 57.50
                                                    return 'Rain'
                                            else:  # pres > 1010.50
                                                if dew_point <= 22.50:
                                                    return 'Cloudy'
                                                else:  # dew_point > 22.50
                                                    return 'Rain'
                                    else:  # dew_point > 24.48
                                        if temp <= 33.50:
                                            if month <= 11.50:
                                                if rhum <= 68.50:
                                                    return 'Rain'
                                                else:  # rhum > 68.50
                                                    return 'Rain'
                                            else:  # month > 11.50
                                                if dew_point <= 25.00:
                                                    return 'Rain'
                                                else:  # dew_point > 25.00
                                                    return 'Rain'
                                        else:  # temp > 33.50
                                            return 'Fog'
                    else:  # latitude > 15.70
                        if latitude <= 34.10:
                            if hour <= 2.50:
                                if pres <= 1013.65:
                                    if month <= 9.50:
                                        if latitude <= 31.28:
                                            if pres <= 1011.25:
                                                if pres <= 1005.10:
                                                    return 'Fog'
                                                else:  # pres > 1005.10
                                                    return 'Fog'
                                            else:  # pres > 1011.25
                                                if month <= 7.50:
                                                    return 'Clear'
                                                else:  # month > 7.50
                                                    return 'Clear'
                                        else:  # latitude > 31.28
                                            if pres <= 1010.60:
                                                if pres <= 1008.55:
                                                    return 'Clear'
                                                else:  # pres > 1008.55
                                                    return 'Cloudy'
                                            else:  # pres > 1010.60
                                                if dew_point <= 22.19:
                                                    return 'Cloudy'
                                                else:  # dew_point > 22.19
                                                    return 'Fog'
                                    else:  # month > 9.50
                                        if pres <= 1009.50:
                                            return 'Clear'
                                        else:  # pres > 1009.50
                                            if temp <= 24.90:
                                                if rhum <= 92.50:
                                                    return 'Clear'
                                                else:  # rhum > 92.50
                                                    return 'Fog'
                                            else:  # temp > 24.90
                                                if rhum <= 87.50:
                                                    return 'Fog'
                                                else:  # rhum > 87.50
                                                    return 'Fog'
                                else:  # pres > 1013.65
                                    if month <= 7.50:
                                        if dew_point <= 22.22:
                                            return 'Clear'
                                        else:  # dew_point > 22.22
                                            return 'Cloudy'
                                    else:  # month > 7.50
                                        return 'Clear'
                            else:  # hour > 2.50
                                if rhum <= 82.50:
                                    if pres <= 1011.05:
                                        if pres <= 1009.30:
                                            if pres <= 1006.05:
                                                if month <= 7.50:
                                                    return 'Fog'
                                                else:  # month > 7.50
                                                    return 'Fog'
                                            else:  # pres > 1006.05
                                                if temp <= 26.75:
                                                    return 'Fog'
                                                else:  # temp > 26.75
                                                    return 'Clear'
                                        else:  # pres > 1009.30
                                            if rhum <= 79.50:
                                                if pres <= 1010.15:
                                                    return 'Fog'
                                                else:  # pres > 1010.15
                                                    return 'Fog'
                                            else:  # rhum > 79.50
                                                if pres <= 1009.75:
                                                    return 'Clear'
                                                else:  # pres > 1009.75
                                                    return 'Clear'
                                    else:  # pres > 1011.05
                                        return 'Clear'
                                else:  # rhum > 82.50
                                    if latitude <= 31.28:
                                        if pres <= 1014.15:
                                            if rhum <= 87.50:
                                                if temp <= 24.95:
                                                    return 'Fog'
                                                else:  # temp > 24.95
                                                    return 'Fog'
                                            else:  # rhum > 87.50
                                                if pres <= 1008.40:
                                                    return 'Fog'
                                                else:  # pres > 1008.40
                                                    return 'Fog'
                                        else:  # pres > 1014.15
                                            if temp <= 24.20:
                                                if dew_point <= 21.98:
                                                    return 'Clear'
                                                else:  # dew_point > 21.98
                                                    return 'Fog'
                                            else:  # temp > 24.20
                                                if dew_point <= 22.01:
                                                    return 'Clear'
                                                else:  # dew_point > 22.01
                                                    return 'Clear'
                                    else:  # latitude > 31.28
                                        if temp <= 23.60:
                                            if pres <= 1013.35:
                                                if pres <= 1012.65:
                                                    return 'Cloudy'
                                                else:  # pres > 1012.65
                                                    return 'Cloudy'
                                            else:  # pres > 1013.35
                                                if pres <= 1013.95:
                                                    return 'Clear'
                                                else:  # pres > 1013.95
                                                    return 'Clear'
                                        else:  # temp > 23.60
                                            return 'Fog'
                        else:  # latitude > 34.10
                            if rhum <= 76.50:
                                if dew_point <= 26.56:
                                    if rhum <= 69.50:
                                        if temp <= 32.15:
                                            if pres <= 1009.95:
                                                if pres <= 1008.45:
                                                    return 'Clear'
                                                else:  # pres > 1008.45
                                                    return 'Clear'
                                            else:  # pres > 1009.95
                                                if month <= 8.50:
                                                    return 'Clear'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                        else:  # temp > 32.15
                                            if month <= 8.50:
                                                return 'Clear'
                                            else:  # month > 8.50
                                                if hour <= 4.50:
                                                    return 'Clear'
                                                else:  # hour > 4.50
                                                    return 'Clear'
                                    else:  # rhum > 69.50
                                        if hour <= 1.50:
                                            if temp <= 26.85:
                                                return 'Cloudy'
                                            else:  # temp > 26.85
                                                if dew_point <= 21.95:
                                                    return 'Cloudy'
                                                else:  # dew_point > 21.95
                                                    return 'Clear'
                                        else:  # hour > 1.50
                                            if pres <= 1008.65:
                                                if dew_point <= 24.89:
                                                    return 'Rain'
                                                else:  # dew_point > 24.89
                                                    return 'Clear'
                                            else:  # pres > 1008.65
                                                if rhum <= 74.50:
                                                    return 'Clear'
                                                else:  # rhum > 74.50
                                                    return 'Rain'
                                else:  # dew_point > 26.56
                                    if dew_point <= 26.57:
                                        return 'Storm'
                                    else:  # dew_point > 26.57
                                        if dew_point <= 26.60:
                                            return 'Clear'
                                        else:  # dew_point > 26.60
                                            return 'Clear'
                            else:  # rhum > 76.50
                                if rhum <= 81.50:
                                    if pres <= 1010.85:
                                        if hour <= 1.50:
                                            if pres <= 1009.95:
                                                if pres <= 1005.35:
                                                    return 'Rain'
                                                else:  # pres > 1005.35
                                                    return 'Clear'
                                            else:  # pres > 1009.95
                                                return 'Rain'
                                        else:  # hour > 1.50
                                            if month <= 9.50:
                                                if temp <= 27.75:
                                                    return 'Rain'
                                                else:  # temp > 27.75
                                                    return 'Rain'
                                            else:  # month > 9.50
                                                return 'Clear'
                                    else:  # pres > 1010.85
                                        if hour <= 0.50:
                                            if dew_point <= 22.50:
                                                if pres <= 1016.55:
                                                    return 'Cloudy'
                                                else:  # pres > 1016.55
                                                    return 'Clear'
                                            else:  # dew_point > 22.50
                                                return 'Clear'
                                        else:  # hour > 0.50
                                            if dew_point <= 22.28:
                                                return 'Clear'
                                            else:  # dew_point > 22.28
                                                if temp <= 27.85:
                                                    return 'Rain'
                                                else:  # temp > 27.85
                                                    return 'Clear'
                                else:  # rhum > 81.50
                                    if dew_point <= 26.12:
                                        if pres <= 1011.25:
                                            if month <= 8.50:
                                                if temp <= 26.45:
                                                    return 'Rain'
                                                else:  # temp > 26.45
                                                    return 'Rain'
                                            else:  # month > 8.50
                                                if rhum <= 82.50:
                                                    return 'Clear'
                                                else:  # rhum > 82.50
                                                    return 'Rain'
                                        else:  # pres > 1011.25
                                            if rhum <= 88.50:
                                                if dew_point <= 22.64:
                                                    return 'Clear'
                                                else:  # dew_point > 22.64
                                                    return 'Rain'
                                            else:  # rhum > 88.50
                                                if temp <= 26.55:
                                                    return 'Rain'
                                                else:  # temp > 26.55
                                                    return 'Clear'
                                    else:  # dew_point > 26.12
                                        if dew_point <= 26.17:
                                            if pres <= 1011.75:
                                                return 'Clear'
                                            else:  # pres > 1011.75
                                                return 'Storm'
                                        else:  # dew_point > 26.17
                                            if temp <= 28.45:
                                                if temp <= 27.65:
                                                    return 'Rain'
                                                else:  # temp > 27.65
                                                    return 'Clear'
                                            else:  # temp > 28.45
                                                if pres <= 1014.05:
                                                    return 'Rain'
                                                else:  # pres > 1014.05
                                                    return 'Clear'
                else:  # hour > 5.50
                    if latitude <= 15.70:
                        if hour <= 12.50:
                            if hour <= 6.50:
                                if dew_point <= 25.09:
                                    if temp <= 30.50:
                                        if month <= 11.50:
                                            if month <= 3.50:
                                                if temp <= 26.30:
                                                    return 'Rain'
                                                else:  # temp > 26.30
                                                    return 'Storm'
                                            else:  # month > 3.50
                                                if dew_point <= 23.49:
                                                    return 'Storm'
                                                else:  # dew_point > 23.49
                                                    return 'Storm'
                                        else:  # month > 11.50
                                            if dew_point <= 23.91:
                                                if pres <= 1010.50:
                                                    return 'Rain'
                                                else:  # pres > 1010.50
                                                    return 'Rain'
                                            else:  # dew_point > 23.91
                                                if dew_point <= 25.04:
                                                    return 'Storm'
                                                else:  # dew_point > 25.04
                                                    return 'Rain'
                                    else:  # temp > 30.50
                                        if month <= 5.50:
                                            if pres <= 1008.05:
                                                if dew_point <= 24.03:
                                                    return 'Rain'
                                                else:  # dew_point > 24.03
                                                    return 'Rain'
                                            else:  # pres > 1008.05
                                                if latitude <= -16.26:
                                                    return 'Storm'
                                                else:  # latitude > -16.26
                                                    return 'Storm'
                                        else:  # month > 5.50
                                            if pres <= 1008.50:
                                                if dew_point <= 24.48:
                                                    return 'Storm'
                                                else:  # dew_point > 24.48
                                                    return 'Rain'
                                            else:  # pres > 1008.50
                                                if dew_point <= 22.50:
                                                    return 'Storm'
                                                else:  # dew_point > 22.50
                                                    return 'Rain'
                                else:  # dew_point > 25.09
                                    if pres <= 1006.50:
                                        if dew_point <= 25.11:
                                            if month <= 4.50:
                                                return 'Rain'
                                            else:  # month > 4.50
                                                return 'Storm'
                                        else:  # dew_point > 25.11
                                            if temp <= 31.50:
                                                return 'Cloudy'
                                            else:  # temp > 31.50
                                                if dew_point <= 25.60:
                                                    return 'Rain'
                                                else:  # dew_point > 25.60
                                                    return 'Rain'
                                    else:  # pres > 1006.50
                                        if dew_point <= 26.02:
                                            if dew_point <= 25.95:
                                                if rhum <= 80.50:
                                                    return 'Rain'
                                                else:  # rhum > 80.50
                                                    return 'Rain'
                                            else:  # dew_point > 25.95
                                                if pres <= 1009.50:
                                                    return 'Rain'
                                                else:  # pres > 1009.50
                                                    return 'Cloudy'
                                        else:  # dew_point > 26.02
                                            if pres <= 1011.50:
                                                if month <= 4.50:
                                                    return 'Rain'
                                                else:  # month > 4.50
                                                    return 'Rain'
                                            else:  # pres > 1011.50
                                                return 'Cloudy'
                            else:  # hour > 6.50
                                if hour <= 11.50:
                                    if month <= 5.50:
                                        if latitude <= -11.10:
                                            if hour <= 7.50:
                                                if dew_point <= 22.19:
                                                    return 'Storm'
                                                else:  # dew_point > 22.19
                                                    return 'Rain'
                                            else:  # hour > 7.50
                                                if temp <= 25.15:
                                                    return 'Rain'
                                                else:  # temp > 25.15
                                                    return 'Clear'
                                        else:  # latitude > -11.10
                                            if month <= 2.50:
                                                if temp <= 23.50:
                                                    return 'Rain'
                                                else:  # temp > 23.50
                                                    return 'Storm'
                                            else:  # month > 2.50
                                                if dew_point <= 26.97:
                                                    return 'Storm'
                                                else:  # dew_point > 26.97
                                                    return 'Rain'
                                    else:  # month > 5.50
                                        if dew_point <= 25.09:
                                            if month <= 8.50:
                                                if month <= 6.50:
                                                    return 'Storm'
                                                else:  # month > 6.50
                                                    return 'Storm'
                                            else:  # month > 8.50
                                                if dew_point <= 24.07:
                                                    return 'Storm'
                                                else:  # dew_point > 24.07
                                                    return 'Storm'
                                        else:  # dew_point > 25.09
                                            if pres <= 1006.50:
                                                if month <= 8.50:
                                                    return 'Rain'
                                                else:  # month > 8.50
                                                    return 'Storm'
                                            else:  # pres > 1006.50
                                                if hour <= 8.50:
                                                    return 'Rain'
                                                else:  # hour > 8.50
                                                    return 'Cloudy'
                                else:  # hour > 11.50
                                    if dew_point <= 25.52:
                                        if month <= 8.50:
                                            if month <= 5.50:
                                                if month <= 3.50:
                                                    return 'Storm'
                                                else:  # month > 3.50
                                                    return 'Storm'
                                            else:  # month > 5.50
                                                if temp <= 26.50:
                                                    return 'Storm'
                                                else:  # temp > 26.50
                                                    return 'Cloudy'
                                        else:  # month > 8.50
                                            if pres <= 1010.50:
                                                if rhum <= 97.00:
                                                    return 'Storm'
                                                else:  # rhum > 97.00
                                                    return 'Cloudy'
                                            else:  # pres > 1010.50
                                                if dew_point <= 24.05:
                                                    return 'Rain'
                                                else:  # dew_point > 24.05
                                                    return 'Storm'
                                    else:  # dew_point > 25.52
                                        if month <= 3.50:
                                            if month <= 2.50:
                                                return 'Clear'
                                            else:  # month > 2.50
                                                return 'Storm'
                                        else:  # month > 3.50
                                            if pres <= 1007.50:
                                                if pres <= 1006.50:
                                                    return 'Rain'
                                                else:  # pres > 1006.50
                                                    return 'Rain'
                                            else:  # pres > 1007.50
                                                if month <= 5.50:
                                                    return 'Rain'
                                                else:  # month > 5.50
                                                    return 'Cloudy'
                        else:  # hour > 12.50
                            if month <= 8.50:
                                if month <= 5.50:
                                    if rhum <= 91.50:
                                        if month <= 2.50:
                                            if pres <= 1008.50:
                                                if temp <= 26.50:
                                                    return 'Rain'
                                                else:  # temp > 26.50
                                                    return 'Cloudy'
                                            else:  # pres > 1008.50
                                                if temp <= 26.65:
                                                    return 'Storm'
                                                else:  # temp > 26.65
                                                    return 'Storm'
                                        else:  # month > 2.50
                                            if month <= 3.50:
                                                if pres <= 1009.95:
                                                    return 'Rain'
                                                else:  # pres > 1009.95
                                                    return 'Cloudy'
                                            else:  # month > 3.50
                                                if dew_point <= 23.49:
                                                    return 'Rain'
                                                else:  # dew_point > 23.49
                                                    return 'Storm'
                                    else:  # rhum > 91.50
                                        if temp <= 27.50:
                                            if pres <= 1009.55:
                                                if pres <= 1009.05:
                                                    return 'Rain'
                                                else:  # pres > 1009.05
                                                    return 'Cloudy'
                                            else:  # pres > 1009.55
                                                if temp <= 24.50:
                                                    return 'Rain'
                                                else:  # temp > 24.50
                                                    return 'Rain'
                                        else:  # temp > 27.50
                                            if pres <= 1008.00:
                                                return 'Cloudy'
                                            else:  # pres > 1008.00
                                                return 'Clear'
                                else:  # month > 5.50
                                    if temp <= 26.50:
                                        if pres <= 1009.50:
                                            if dew_point <= 23.53:
                                                if pres <= 1008.90:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.90
                                                    return 'Rain'
                                            else:  # dew_point > 23.53
                                                if pres <= 1007.50:
                                                    return 'Rain'
                                                else:  # pres > 1007.50
                                                    return 'Cloudy'
                                        else:  # pres > 1009.50
                                            if rhum <= 91.50:
                                                if month <= 7.50:
                                                    return 'Storm'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                            else:  # rhum > 91.50
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Cloudy'
                                    else:  # temp > 26.50
                                        if temp <= 28.50:
                                            if rhum <= 91.50:
                                                if dew_point <= 24.55:
                                                    return 'Cloudy'
                                                else:  # dew_point > 24.55
                                                    return 'Cloudy'
                                            else:  # rhum > 91.50
                                                if pres <= 1008.00:
                                                    return 'Rain'
                                                else:  # pres > 1008.00
                                                    return 'Fog'
                                        else:  # temp > 28.50
                                            if pres <= 1011.50:
                                                if month <= 6.50:
                                                    return 'Cloudy'
                                                else:  # month > 6.50
                                                    return 'Cloudy'
                                            else:  # pres > 1011.50
                                                if pres <= 1012.50:
                                                    return 'Rain'
                                                else:  # pres > 1012.50
                                                    return 'Cloudy'
                            else:  # month > 8.50
                                if temp <= 25.50:
                                    if month <= 9.50:
                                        if rhum <= 91.50:
                                            if pres <= 1010.50:
                                                if pres <= 1009.00:
                                                    return 'Rain'
                                                else:  # pres > 1009.00
                                                    return 'Cloudy'
                                            else:  # pres > 1010.50
                                                if dew_point <= 22.57:
                                                    return 'Cloudy'
                                                else:  # dew_point > 22.57
                                                    return 'Storm'
                                        else:  # rhum > 91.50
                                            if dew_point <= 24.50:
                                                return 'Rain'
                                            else:  # dew_point > 24.50
                                                return 'Cloudy'
                                    else:  # month > 9.50
                                        if dew_point <= 23.51:
                                            if rhum <= 88.00:
                                                return 'Clear'
                                            else:  # rhum > 88.00
                                                if month <= 11.50:
                                                    return 'Rain'
                                                else:  # month > 11.50
                                                    return 'Rain'
                                        else:  # dew_point > 23.51
                                            if month <= 10.50:
                                                if pres <= 1009.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1009.50
                                                    return 'Cloudy'
                                            else:  # month > 10.50
                                                if pres <= 1008.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.50
                                                    return 'Rain'
                                else:  # temp > 25.50
                                    if temp <= 28.50:
                                        if pres <= 1009.70:
                                            if pres <= 1007.50:
                                                if dew_point <= 24.03:
                                                    return 'Cloudy'
                                                else:  # dew_point > 24.03
                                                    return 'Rain'
                                            else:  # pres > 1007.50
                                                if dew_point <= 25.50:
                                                    return 'Storm'
                                                else:  # dew_point > 25.50
                                                    return 'Rain'
                                        else:  # pres > 1009.70
                                            if dew_point <= 24.03:
                                                if month <= 11.50:
                                                    return 'Cloudy'
                                                else:  # month > 11.50
                                                    return 'Rain'
                                            else:  # dew_point > 24.03
                                                if dew_point <= 25.04:
                                                    return 'Storm'
                                                else:  # dew_point > 25.04
                                                    return 'Cloudy'
                                    else:  # temp > 28.50
                                        if pres <= 1009.50:
                                            if dew_point <= 24.46:
                                                if month <= 10.50:
                                                    return 'Cloudy'
                                                else:  # month > 10.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 24.46
                                                if dew_point <= 25.47:
                                                    return 'Rain'
                                                else:  # dew_point > 25.47
                                                    return 'Cloudy'
                                        else:  # pres > 1009.50
                                            if dew_point <= 24.44:
                                                if month <= 9.50:
                                                    return 'Storm'
                                                else:  # month > 9.50
                                                    return 'Cloudy'
                                            else:  # dew_point > 24.44
                                                if rhum <= 81.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 81.50
                                                    return 'Cloudy'
                    else:  # latitude > 15.70
                        if latitude <= 34.10:
                            if dew_point <= 22.06:
                                if month <= 9.50:
                                    if pres <= 1013.20:
                                        if hour <= 8.50:
                                            if pres <= 1005.95:
                                                if rhum <= 83.50:
                                                    return 'Fog'
                                                else:  # rhum > 83.50
                                                    return 'Clear'
                                            else:  # pres > 1005.95
                                                if pres <= 1006.90:
                                                    return 'Clear'
                                                else:  # pres > 1006.90
                                                    return 'Fog'
                                        else:  # hour > 8.50
                                            return 'Clear'
                                    else:  # pres > 1013.20
                                        return 'Clear'
                                else:  # month > 9.50
                                    if dew_point <= 22.03:
                                        return 'Fog'
                                    else:  # dew_point > 22.03
                                        return 'Clear'
                            else:  # dew_point > 22.06
                                if hour <= 9.50:
                                    if pres <= 1004.30:
                                        return 'Clear'
                                    else:  # pres > 1004.30
                                        if pres <= 1006.60:
                                            if pres <= 1005.15:
                                                return 'Fog'
                                            else:  # pres > 1005.15
                                                if temp <= 26.45:
                                                    return 'Clear'
                                                else:  # temp > 26.45
                                                    return 'Fog'
                                        else:  # pres > 1006.60
                                            if rhum <= 58.50:
                                                return 'Clear'
                                            else:  # rhum > 58.50
                                                if month <= 9.50:
                                                    return 'Fog'
                                                else:  # month > 9.50
                                                    return 'Fog'
                                else:  # hour > 9.50
                                    if hour <= 10.50:
                                        return 'Clear'
                                    else:  # hour > 10.50
                                        return 'Clear'
                        else:  # latitude > 34.10
                            if rhum <= 85.50:
                                if dew_point <= 25.46:
                                    if temp <= 27.25:
                                        if hour <= 11.50:
                                            if pres <= 1010.25:
                                                if hour <= 9.50:
                                                    return 'Rain'
                                                else:  # hour > 9.50
                                                    return 'Rain'
                                            else:  # pres > 1010.25
                                                if temp <= 25.85:
                                                    return 'Rain'
                                                else:  # temp > 25.85
                                                    return 'Clear'
                                        else:  # hour > 11.50
                                            if temp <= 25.30:
                                                if rhum <= 84.50:
                                                    return 'Rain'
                                                else:  # rhum > 84.50
                                                    return 'Clear'
                                            else:  # temp > 25.30
                                                if month <= 8.50:
                                                    return 'Clear'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                    else:  # temp > 27.25
                                        if month <= 8.50:
                                            if temp <= 29.25:
                                                if hour <= 8.50:
                                                    return 'Rain'
                                                else:  # hour > 8.50
                                                    return 'Clear'
                                            else:  # temp > 29.25
                                                if pres <= 996.70:
                                                    return 'Rain'
                                                else:  # pres > 996.70
                                                    return 'Clear'
                                        else:  # month > 8.50
                                            if temp <= 32.55:
                                                if dew_point <= 23.78:
                                                    return 'Clear'
                                                else:  # dew_point > 23.78
                                                    return 'Clear'
                                            else:  # temp > 32.55
                                                if rhum <= 60.00:
                                                    return 'Clear'
                                                else:  # rhum > 60.00
                                                    return 'Storm'
                                else:  # dew_point > 25.46
                                    if pres <= 1004.00:
                                        return 'Storm'
                                    else:  # pres > 1004.00
                                        if pres <= 1007.10:
                                            if temp <= 29.65:
                                                if hour <= 6.50:
                                                    return 'Clear'
                                                else:  # hour > 6.50
                                                    return 'Rain'
                                            else:  # temp > 29.65
                                                if hour <= 9.50:
                                                    return 'Clear'
                                                else:  # hour > 9.50
                                                    return 'Rain'
                                        else:  # pres > 1007.10
                                            if dew_point <= 26.24:
                                                return 'Clear'
                                            else:  # dew_point > 26.24
                                                if hour <= 6.50:
                                                    return 'Rain'
                                                else:  # hour > 6.50
                                                    return 'Clear'
                            else:  # rhum > 85.50
                                if pres <= 1012.55:
                                    if temp <= 25.15:
                                        if pres <= 1010.55:
                                            if dew_point <= 24.83:
                                                if pres <= 1008.95:
                                                    return 'Rain'
                                                else:  # pres > 1008.95
                                                    return 'Rain'
                                            else:  # dew_point > 24.83
                                                return 'Clear'
                                        else:  # pres > 1010.55
                                            if rhum <= 94.00:
                                                if pres <= 1012.10:
                                                    return 'Clear'
                                                else:  # pres > 1012.10
                                                    return 'Rain'
                                            else:  # rhum > 94.00
                                                if pres <= 1012.45:
                                                    return 'Rain'
                                                else:  # pres > 1012.45
                                                    return 'Clear'
                                    else:  # temp > 25.15
                                        if temp <= 25.55:
                                            if dew_point <= 25.45:
                                                if pres <= 1010.65:
                                                    return 'Rain'
                                                else:  # pres > 1010.65
                                                    return 'Clear'
                                            else:  # dew_point > 25.45
                                                return 'Storm'
                                        else:  # temp > 25.55
                                            if hour <= 10.50:
                                                if temp <= 28.25:
                                                    return 'Rain'
                                                else:  # temp > 28.25
                                                    return 'Clear'
                                            else:  # hour > 10.50
                                                if pres <= 1010.55:
                                                    return 'Rain'
                                                else:  # pres > 1010.55
                                                    return 'Clear'
                                else:  # pres > 1012.55
                                    if rhum <= 96.50:
                                        if dew_point <= 25.72:
                                            if hour <= 11.50:
                                                if rhum <= 87.50:
                                                    return 'Clear'
                                                else:  # rhum > 87.50
                                                    return 'Rain'
                                            else:  # hour > 11.50
                                                if pres <= 1017.55:
                                                    return 'Clear'
                                                else:  # pres > 1017.55
                                                    return 'Rain'
                                        else:  # dew_point > 25.72
                                            return 'Rain'
                                    else:  # rhum > 96.50
                                        if temp <= 25.55:
                                            if hour <= 6.50:
                                                return 'Storm'
                                            else:  # hour > 6.50
                                                if pres <= 1013.65:
                                                    return 'Rain'
                                                else:  # pres > 1013.65
                                                    return 'Rain'
                                        else:  # temp > 25.55
                                            if pres <= 1013.10:
                                                return 'Rain'
                                            else:  # pres > 1013.10
                                                if month <= 8.00:
                                                    return 'Clear'
                                                else:  # month > 8.00
                                                    return 'Storm'
            else:  # hour > 13.50
                if latitude <= 15.70:
                    if rhum <= 92.50:
                        if hour <= 21.50:
                            if latitude <= -11.10:
                                if temp <= 28.50:
                                    if pres <= 1012.75:
                                        if dew_point <= 23.08:
                                            if temp <= 25.55:
                                                if rhum <= 86.50:
                                                    return 'Clear'
                                                else:  # rhum > 86.50
                                                    return 'Rain'
                                            else:  # temp > 25.55
                                                if hour <= 16.00:
                                                    return 'Cloudy'
                                                else:  # hour > 16.00
                                                    return 'Rain'
                                        else:  # dew_point > 23.08
                                            return 'Fog'
                                    else:  # pres > 1012.75
                                        if dew_point <= 22.68:
                                            if pres <= 1014.10:
                                                if hour <= 18.50:
                                                    return 'Fog'
                                                else:  # hour > 18.50
                                                    return 'Storm'
                                            else:  # pres > 1014.10
                                                if rhum <= 80.00:
                                                    return 'Rain'
                                                else:  # rhum > 80.00
                                                    return 'Fog'
                                        else:  # dew_point > 22.68
                                            return 'Storm'
                                else:  # temp > 28.50
                                    if pres <= 1016.50:
                                        return 'Rain'
                                    else:  # pres > 1016.50
                                        return 'Clear'
                            else:  # latitude > -11.10
                                if month <= 2.50:
                                    if temp <= 24.50:
                                        if hour <= 15.50:
                                            if pres <= 1010.50:
                                                return 'Rain'
                                            else:  # pres > 1010.50
                                                if hour <= 14.50:
                                                    return 'Rain'
                                                else:  # hour > 14.50
                                                    return 'Rain'
                                        else:  # hour > 15.50
                                            if hour <= 16.50:
                                                return 'Cloudy'
                                            else:  # hour > 16.50
                                                if pres <= 1010.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1010.50
                                                    return 'Rain'
                                    else:  # temp > 24.50
                                        if hour <= 14.50:
                                            if rhum <= 81.50:
                                                if pres <= 1009.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1009.50
                                                    return 'Cloudy'
                                            else:  # rhum > 81.50
                                                if pres <= 1010.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1010.50
                                                    return 'Cloudy'
                                        else:  # hour > 14.50
                                            if rhum <= 86.50:
                                                if pres <= 1011.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.50
                                                    return 'Cloudy'
                                            else:  # rhum > 86.50
                                                if pres <= 1012.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1012.50
                                                    return 'Cloudy'
                                else:  # month > 2.50
                                    if month <= 5.50:
                                        if hour <= 15.50:
                                            if pres <= 1010.60:
                                                if dew_point <= 25.01:
                                                    return 'Rain'
                                                else:  # dew_point > 25.01
                                                    return 'Rain'
                                            else:  # pres > 1010.60
                                                if dew_point <= 26.02:
                                                    return 'Rain'
                                                else:  # dew_point > 26.02
                                                    return 'Storm'
                                        else:  # hour > 15.50
                                            if hour <= 17.50:
                                                if pres <= 1010.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1010.95
                                                    return 'Cloudy'
                                            else:  # hour > 17.50
                                                if pres <= 1008.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.95
                                                    return 'Cloudy'
                                    else:  # month > 5.50
                                        if temp <= 26.50:
                                            if month <= 10.50:
                                                if temp <= 24.50:
                                                    return 'Storm'
                                                else:  # temp > 24.50
                                                    return 'Cloudy'
                                            else:  # month > 10.50
                                                if hour <= 14.50:
                                                    return 'Rain'
                                                else:  # hour > 14.50
                                                    return 'Cloudy'
                                        else:  # temp > 26.50
                                            if temp <= 27.40:
                                                if hour <= 14.50:
                                                    return 'Cloudy'
                                                else:  # hour > 14.50
                                                    return 'Cloudy'
                                            else:  # temp > 27.40
                                                if dew_point <= 24.07:
                                                    return 'Cloudy'
                                                else:  # dew_point > 24.07
                                                    return 'Cloudy'
                        else:  # hour > 21.50
                            if month <= 4.50:
                                if pres <= 1014.50:
                                    if rhum <= 85.50:
                                        if latitude <= -11.10:
                                            if rhum <= 81.50:
                                                if dew_point <= 22.55:
                                                    return 'Rain'
                                                else:  # dew_point > 22.55
                                                    return 'Clear'
                                            else:  # rhum > 81.50
                                                return 'Cloudy'
                                        else:  # latitude > -11.10
                                            if pres <= 1008.05:
                                                if pres <= 1007.95:
                                                    return 'Cloudy'
                                                else:  # pres > 1007.95
                                                    return 'Rain'
                                            else:  # pres > 1008.05
                                                if dew_point <= 23.07:
                                                    return 'Cloudy'
                                                else:  # dew_point > 23.07
                                                    return 'Cloudy'
                                    else:  # rhum > 85.50
                                        if dew_point <= 24.54:
                                            if pres <= 1007.55:
                                                if month <= 2.50:
                                                    return 'Fog'
                                                else:  # month > 2.50
                                                    return 'Rain'
                                            else:  # pres > 1007.55
                                                if latitude <= -16.26:
                                                    return 'Rain'
                                                else:  # latitude > -16.26
                                                    return 'Cloudy'
                                        else:  # dew_point > 24.54
                                            if pres <= 1009.50:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                            else:  # pres > 1009.50
                                                if hour <= 22.50:
                                                    return 'Cloudy'
                                                else:  # hour > 22.50
                                                    return 'Storm'
                                else:  # pres > 1014.50
                                    if latitude <= -28.71:
                                        return 'Clear'
                                    else:  # latitude > -28.71
                                        return 'Storm'
                            else:  # month > 4.50
                                if temp <= 25.50:
                                    if month <= 10.50:
                                        if rhum <= 86.50:
                                            if hour <= 22.50:
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Storm'
                                            else:  # hour > 22.50
                                                return 'Rain'
                                        else:  # rhum > 86.50
                                            if month <= 9.50:
                                                if pres <= 1009.50:
                                                    return 'Storm'
                                                else:  # pres > 1009.50
                                                    return 'Storm'
                                            else:  # month > 9.50
                                                if pres <= 1008.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1008.50
                                                    return 'Rain'
                                    else:  # month > 10.50
                                        if month <= 11.50:
                                            if pres <= 1009.50:
                                                if pres <= 1007.50:
                                                    return 'Rain'
                                                else:  # pres > 1007.50
                                                    return 'Fog'
                                            else:  # pres > 1009.50
                                                if rhum <= 86.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 86.50
                                                    return 'Rain'
                                        else:  # month > 11.50
                                            if latitude <= -28.71:
                                                return 'Rain'
                                            else:  # latitude > -28.71
                                                if pres <= 1008.50:
                                                    return 'Rain'
                                                else:  # pres > 1008.50
                                                    return 'Cloudy'
                                else:  # temp > 25.50
                                    if month <= 11.50:
                                        if pres <= 1009.70:
                                            if dew_point <= 25.04:
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Rain'
                                            else:  # dew_point > 25.04
                                                if month <= 5.50:
                                                    return 'Storm'
                                                else:  # month > 5.50
                                                    return 'Cloudy'
                                        else:  # pres > 1009.70
                                            if month <= 10.50:
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Fog'
                                            else:  # month > 10.50
                                                if dew_point <= 24.55:
                                                    return 'Fog'
                                                else:  # dew_point > 24.55
                                                    return 'Storm'
                                    else:  # month > 11.50
                                        if dew_point <= 24.55:
                                            if pres <= 1011.10:
                                                if pres <= 1009.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1009.50
                                                    return 'Cloudy'
                                            else:  # pres > 1011.10
                                                if rhum <= 76.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 76.50
                                                    return 'Cloudy'
                                        else:  # dew_point > 24.55
                                            if hour <= 22.50:
                                                return 'Rain'
                                            else:  # hour > 22.50
                                                return 'Storm'
                    else:  # rhum > 92.50
                        if dew_point <= 23.02:
                            if pres <= 1010.50:
                                if month <= 3.50:
                                    if month <= 1.50:
                                        if dew_point <= 22.99:
                                            if pres <= 1007.50:
                                                if hour <= 20.50:
                                                    return 'Rain'
                                                else:  # hour > 20.50
                                                    return 'Rain'
                                            else:  # pres > 1007.50
                                                if hour <= 18.50:
                                                    return 'Rain'
                                                else:  # hour > 18.50
                                                    return 'Rain'
                                        else:  # dew_point > 22.99
                                            if hour <= 20.00:
                                                return 'Rain'
                                            else:  # hour > 20.00
                                                return 'Rain'
                                    else:  # month > 1.50
                                        if latitude <= -16.26:
                                            if hour <= 21.50:
                                                if pres <= 1005.85:
                                                    return 'Rain'
                                                else:  # pres > 1005.85
                                                    return 'Rain'
                                            else:  # hour > 21.50
                                                return 'Cloudy'
                                        else:  # latitude > -16.26
                                            if hour <= 16.00:
                                                return 'Rain'
                                            else:  # hour > 16.00
                                                if pres <= 1006.90:
                                                    return 'Rain'
                                                else:  # pres > 1006.90
                                                    return 'Cloudy'
                                else:  # month > 3.50
                                    if month <= 4.50:
                                        if pres <= 1009.75:
                                            if hour <= 21.50:
                                                if pres <= 1008.00:
                                                    return 'Rain'
                                                else:  # pres > 1008.00
                                                    return 'Rain'
                                            else:  # hour > 21.50
                                                if hour <= 22.50:
                                                    return 'Cloudy'
                                                else:  # hour > 22.50
                                                    return 'Cloudy'
                                        else:  # pres > 1009.75
                                            if hour <= 22.00:
                                                return 'Storm'
                                            else:  # hour > 22.00
                                                if dew_point <= 22.48:
                                                    return 'Rain'
                                                else:  # dew_point > 22.48
                                                    return 'Cloudy'
                                    else:  # month > 4.50
                                        if month <= 9.50:
                                            if hour <= 22.50:
                                                if pres <= 1009.50:
                                                    return 'Fog'
                                                else:  # pres > 1009.50
                                                    return 'Rain'
                                            else:  # hour > 22.50
                                                if rhum <= 97.00:
                                                    return 'Fog'
                                                else:  # rhum > 97.00
                                                    return 'Cloudy'
                                        else:  # month > 9.50
                                            if month <= 10.50:
                                                if pres <= 1008.50:
                                                    return 'Storm'
                                                else:  # pres > 1008.50
                                                    return 'Cloudy'
                                            else:  # month > 10.50
                                                if latitude <= -16.26:
                                                    return 'Fog'
                                                else:  # latitude > -16.26
                                                    return 'Rain'
                            else:  # pres > 1010.50
                                if dew_point <= 22.18:
                                    if hour <= 20.50:
                                        if latitude <= -11.10:
                                            if pres <= 1016.50:
                                                return 'Storm'
                                            else:  # pres > 1016.50
                                                if hour <= 16.50:
                                                    return 'Rain'
                                                else:  # hour > 16.50
                                                    return 'Storm'
                                        else:  # latitude > -11.10
                                            if pres <= 1011.50:
                                                if hour <= 18.00:
                                                    return 'Storm'
                                                else:  # hour > 18.00
                                                    return 'Cloudy'
                                            else:  # pres > 1011.50
                                                if dew_point <= 21.99:
                                                    return 'Rain'
                                                else:  # dew_point > 21.99
                                                    return 'Rain'
                                    else:  # hour > 20.50
                                        if dew_point <= 21.93:
                                            return 'Clear'
                                        else:  # dew_point > 21.93
                                            if latitude <= -28.71:
                                                return 'Cloudy'
                                            else:  # latitude > -28.71
                                                if hour <= 21.50:
                                                    return 'Rain'
                                                else:  # hour > 21.50
                                                    return 'Rain'
                                else:  # dew_point > 22.18
                                    if month <= 7.00:
                                        if month <= 3.50:
                                            if pres <= 1012.50:
                                                if temp <= 23.75:
                                                    return 'Rain'
                                                else:  # temp > 23.75
                                                    return 'Rain'
                                            else:  # pres > 1012.50
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Rain'
                                        else:  # month > 3.50
                                            if hour <= 22.50:
                                                if pres <= 1011.50:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.50
                                                    return 'Rain'
                                            else:  # hour > 22.50
                                                if pres <= 1011.50:
                                                    return 'Rain'
                                                else:  # pres > 1011.50
                                                    return 'Fog'
                                    else:  # month > 7.00
                                        if month <= 11.50:
                                            if pres <= 1012.50:
                                                if month <= 9.50:
                                                    return 'Storm'
                                                else:  # month > 9.50
                                                    return 'Storm'
                                            else:  # pres > 1012.50
                                                if month <= 9.50:
                                                    return 'Rain'
                                                else:  # month > 9.50
                                                    return 'Cloudy'
                                        else:  # month > 11.50
                                            if pres <= 1012.60:
                                                if hour <= 18.50:
                                                    return 'Rain'
                                                else:  # hour > 18.50
                                                    return 'Rain'
                                            else:  # pres > 1012.60
                                                return 'Cloudy'
                        else:  # dew_point > 23.02
                            if rhum <= 97.50:
                                if hour <= 21.50:
                                    if pres <= 1012.50:
                                        if hour <= 15.50:
                                            if month <= 5.50:
                                                if dew_point <= 26.45:
                                                    return 'Rain'
                                                else:  # dew_point > 26.45
                                                    return 'Cloudy'
                                            else:  # month > 5.50
                                                if dew_point <= 24.46:
                                                    return 'Rain'
                                                else:  # dew_point > 24.46
                                                    return 'Cloudy'
                                        else:  # hour > 15.50
                                            if month <= 9.50:
                                                if pres <= 1011.60:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.60
                                                    return 'Storm'
                                            else:  # month > 9.50
                                                if temp <= 25.50:
                                                    return 'Cloudy'
                                                else:  # temp > 25.50
                                                    return 'Fog'
                                    else:  # pres > 1012.50
                                        if month <= 6.00:
                                            if month <= 4.00:
                                                if hour <= 16.50:
                                                    return 'Rain'
                                                else:  # hour > 16.50
                                                    return 'Cloudy'
                                            else:  # month > 4.00
                                                if hour <= 15.50:
                                                    return 'Cloudy'
                                                else:  # hour > 15.50
                                                    return 'Storm'
                                        else:  # month > 6.00
                                            if month <= 9.00:
                                                if temp <= 25.50:
                                                    return 'Rain'
                                                else:  # temp > 25.50
                                                    return 'Cloudy'
                                            else:  # month > 9.00
                                                if temp <= 25.50:
                                                    return 'Cloudy'
                                                else:  # temp > 25.50
                                                    return 'Cloudy'
                                else:  # hour > 21.50
                                    if month <= 3.50:
                                        if month <= 1.50:
                                            if pres <= 1009.50:
                                                if hour <= 22.50:
                                                    return 'Cloudy'
                                                else:  # hour > 22.50
                                                    return 'Cloudy'
                                            else:  # pres > 1009.50
                                                if pres <= 1010.50:
                                                    return 'Fog'
                                                else:  # pres > 1010.50
                                                    return 'Cloudy'
                                        else:  # month > 1.50
                                            if pres <= 1007.50:
                                                if dew_point <= 25.45:
                                                    return 'Rain'
                                                else:  # dew_point > 25.45
                                                    return 'Cloudy'
                                            else:  # pres > 1007.50
                                                if temp <= 25.50:
                                                    return 'Cloudy'
                                                else:  # temp > 25.50
                                                    return 'Cloudy'
                                    else:  # month > 3.50
                                        if month <= 4.50:
                                            if hour <= 22.50:
                                                if temp <= 25.50:
                                                    return 'Cloudy'
                                                else:  # temp > 25.50
                                                    return 'Fog'
                                            else:  # hour > 22.50
                                                if dew_point <= 25.45:
                                                    return 'Fog'
                                                else:  # dew_point > 25.45
                                                    return 'Cloudy'
                                        else:  # month > 4.50
                                            if month <= 9.50:
                                                if pres <= 1006.50:
                                                    return 'Fog'
                                                else:  # pres > 1006.50
                                                    return 'Rain'
                                            else:  # month > 9.50
                                                if pres <= 1008.85:
                                                    return 'Rain'
                                                else:  # pres > 1008.85
                                                    return 'Fog'
                            else:  # rhum > 97.50
                                if hour <= 17.50:
                                    if month <= 5.50:
                                        if pres <= 1009.50:
                                            if pres <= 1008.50:
                                                if month <= 4.50:
                                                    return 'Fog'
                                                else:  # month > 4.50
                                                    return 'Rain'
                                            else:  # pres > 1008.50
                                                if hour <= 16.50:
                                                    return 'Rain'
                                                else:  # hour > 16.50
                                                    return 'Fog'
                                        else:  # pres > 1009.50
                                            if temp <= 26.50:
                                                if temp <= 24.50:
                                                    return 'Rain'
                                                else:  # temp > 24.50
                                                    return 'Storm'
                                            else:  # temp > 26.50
                                                if hour <= 15.50:
                                                    return 'Fog'
                                                else:  # hour > 15.50
                                                    return 'Fog'
                                    else:  # month > 5.50
                                        if dew_point <= 24.50:
                                            if pres <= 1010.50:
                                                if hour <= 14.50:
                                                    return 'Rain'
                                                else:  # hour > 14.50
                                                    return 'Cloudy'
                                            else:  # pres > 1010.50
                                                if month <= 8.50:
                                                    return 'Cloudy'
                                                else:  # month > 8.50
                                                    return 'Rain'
                                        else:  # dew_point > 24.50
                                            if pres <= 1011.50:
                                                if month <= 6.50:
                                                    return 'Fog'
                                                else:  # month > 6.50
                                                    return 'Cloudy'
                                            else:  # pres > 1011.50
                                                if dew_point <= 25.50:
                                                    return 'Cloudy'
                                                else:  # dew_point > 25.50
                                                    return 'Fog'
                                else:  # hour > 17.50
                                    if dew_point <= 24.50:
                                        if month <= 3.50:
                                            if pres <= 1008.50:
                                                if month <= 2.50:
                                                    return 'Rain'
                                                else:  # month > 2.50
                                                    return 'Cloudy'
                                            else:  # pres > 1008.50
                                                if pres <= 1009.50:
                                                    return 'Rain'
                                                else:  # pres > 1009.50
                                                    return 'Rain'
                                        else:  # month > 3.50
                                            if month <= 4.50:
                                                if hour <= 22.50:
                                                    return 'Storm'
                                                else:  # hour > 22.50
                                                    return 'Fog'
                                            else:  # month > 4.50
                                                if month <= 6.50:
                                                    return 'Fog'
                                                else:  # month > 6.50
                                                    return 'Cloudy'
                                    else:  # dew_point > 24.50
                                        if pres <= 1010.75:
                                            if hour <= 19.50:
                                                if month <= 4.50:
                                                    return 'Fog'
                                                else:  # month > 4.50
                                                    return 'Cloudy'
                                            else:  # hour > 19.50
                                                if temp <= 26.50:
                                                    return 'Fog'
                                                else:  # temp > 26.50
                                                    return 'Cloudy'
                                        else:  # pres > 1010.75
                                            if pres <= 1012.50:
                                                if month <= 3.50:
                                                    return 'Cloudy'
                                                else:  # month > 3.50
                                                    return 'Fog'
                                            else:  # pres > 1012.50
                                                return 'Rain'
                else:  # latitude > 15.70
                    if rhum <= 93.50:
                        if pres <= 1006.95:
                            if rhum <= 80.50:
                                if dew_point <= 24.98:
                                    if rhum <= 48.00:
                                        if temp <= 36.00:
                                            if pres <= 1005.50:
                                                return 'Fog'
                                            else:  # pres > 1005.50
                                                return 'Clear'
                                        else:  # temp > 36.00
                                            return 'Clear'
                                    else:  # rhum > 48.00
                                        if dew_point <= 24.37:
                                            if pres <= 1003.95:
                                                if dew_point <= 22.47:
                                                    return 'Clear'
                                                else:  # dew_point > 22.47
                                                    return 'Clear'
                                            else:  # pres > 1003.95
                                                if month <= 8.50:
                                                    return 'Clear'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                        else:  # dew_point > 24.37
                                            if hour <= 16.50:
                                                if rhum <= 79.50:
                                                    return 'Cloudy'
                                                else:  # rhum > 79.50
                                                    return 'Clear'
                                            else:  # hour > 16.50
                                                return 'Clear'
                                else:  # dew_point > 24.98
                                    if temp <= 29.20:
                                        if pres <= 1006.20:
                                            return 'Fog'
                                        else:  # pres > 1006.20
                                            return 'Clear'
                                    else:  # temp > 29.20
                                        if pres <= 1001.95:
                                            return 'Rain'
                                        else:  # pres > 1001.95
                                            return 'Clear'
                            else:  # rhum > 80.50
                                if month <= 8.50:
                                    if hour <= 21.50:
                                        if temp <= 26.95:
                                            if dew_point <= 23.72:
                                                if temp <= 25.95:
                                                    return 'Rain'
                                                else:  # temp > 25.95
                                                    return 'Clear'
                                            else:  # dew_point > 23.72
                                                if dew_point <= 25.18:
                                                    return 'Rain'
                                                else:  # dew_point > 25.18
                                                    return 'Clear'
                                        else:  # temp > 26.95
                                            if temp <= 28.35:
                                                if dew_point <= 23.81:
                                                    return 'Rain'
                                                else:  # dew_point > 23.81
                                                    return 'Clear'
                                            else:  # temp > 28.35
                                                if dew_point <= 26.07:
                                                    return 'Rain'
                                                else:  # dew_point > 26.07
                                                    return 'Rain'
                                    else:  # hour > 21.50
                                        if dew_point <= 22.13:
                                            return 'Cloudy'
                                        else:  # dew_point > 22.13
                                            if pres <= 1001.55:
                                                return 'Clear'
                                            else:  # pres > 1001.55
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                else:  # month > 8.50
                                    if temp <= 24.75:
                                        return 'Cloudy'
                                    else:  # temp > 24.75
                                        if hour <= 22.50:
                                            if pres <= 1006.55:
                                                return 'Rain'
                                            else:  # pres > 1006.55
                                                if hour <= 18.50:
                                                    return 'Rain'
                                                else:  # hour > 18.50
                                                    return 'Clear'
                                        else:  # hour > 22.50
                                            return 'Cloudy'
                        else:  # pres > 1006.95
                            if temp <= 25.85:
                                if latitude <= 34.10:
                                    if temp <= 25.30:
                                        if pres <= 1012.70:
                                            if month <= 9.50:
                                                if latitude <= 31.28:
                                                    return 'Clear'
                                                else:  # latitude > 31.28
                                                    return 'Cloudy'
                                            else:  # month > 9.50
                                                return 'Fog'
                                        else:  # pres > 1012.70
                                            return 'Clear'
                                    else:  # temp > 25.30
                                        if hour <= 21.50:
                                            return 'Fog'
                                        else:  # hour > 21.50
                                            return 'Cloudy'
                                else:  # latitude > 34.10
                                    if pres <= 1013.75:
                                        if hour <= 20.50:
                                            if pres <= 1008.25:
                                                if dew_point <= 22.99:
                                                    return 'Clear'
                                                else:  # dew_point > 22.99
                                                    return 'Rain'
                                            else:  # pres > 1008.25
                                                if temp <= 24.95:
                                                    return 'Clear'
                                                else:  # temp > 24.95
                                                    return 'Clear'
                                        else:  # hour > 20.50
                                            if dew_point <= 22.81:
                                                if temp <= 24.85:
                                                    return 'Rain'
                                                else:  # temp > 24.85
                                                    return 'Rain'
                                            else:  # dew_point > 22.81
                                                if month <= 7.50:
                                                    return 'Clear'
                                                else:  # month > 7.50
                                                    return 'Clear'
                                    else:  # pres > 1013.75
                                        if hour <= 21.50:
                                            if pres <= 1017.55:
                                                if rhum <= 92.50:
                                                    return 'Clear'
                                                else:  # rhum > 92.50
                                                    return 'Clear'
                                            else:  # pres > 1017.55
                                                if pres <= 1018.00:
                                                    return 'Rain'
                                                else:  # pres > 1018.00
                                                    return 'Clear'
                                        else:  # hour > 21.50
                                            if rhum <= 89.50:
                                                if pres <= 1019.55:
                                                    return 'Clear'
                                                else:  # pres > 1019.55
                                                    return 'Cloudy'
                                            else:  # rhum > 89.50
                                                return 'Cloudy'
                            else:  # temp > 25.85
                                if dew_point <= 25.60:
                                    if hour <= 21.50:
                                        if pres <= 1009.75:
                                            if temp <= 26.95:
                                                if month <= 7.50:
                                                    return 'Rain'
                                                else:  # month > 7.50
                                                    return 'Clear'
                                            else:  # temp > 26.95
                                                if hour <= 16.50:
                                                    return 'Clear'
                                                else:  # hour > 16.50
                                                    return 'Clear'
                                        else:  # pres > 1009.75
                                            if dew_point <= 21.86:
                                                return 'Cloudy'
                                            else:  # dew_point > 21.86
                                                if hour <= 15.50:
                                                    return 'Clear'
                                                else:  # hour > 15.50
                                                    return 'Clear'
                                    else:  # hour > 21.50
                                        if rhum <= 78.50:
                                            if temp <= 27.20:
                                                if dew_point <= 22.37:
                                                    return 'Clear'
                                                else:  # dew_point > 22.37
                                                    return 'Clear'
                                            else:  # temp > 27.20
                                                if hour <= 22.50:
                                                    return 'Clear'
                                                else:  # hour > 22.50
                                                    return 'Clear'
                                        else:  # rhum > 78.50
                                            if pres <= 1012.05:
                                                if temp <= 26.05:
                                                    return 'Clear'
                                                else:  # temp > 26.05
                                                    return 'Clear'
                                            else:  # pres > 1012.05
                                                if pres <= 1013.65:
                                                    return 'Clear'
                                                else:  # pres > 1013.65
                                                    return 'Clear'
                                else:  # dew_point > 25.60
                                    if temp <= 27.85:
                                        if hour <= 21.50:
                                            if hour <= 20.50:
                                                if pres <= 1010.35:
                                                    return 'Clear'
                                                else:  # pres > 1010.35
                                                    return 'Rain'
                                            else:  # hour > 20.50
                                                return 'Clear'
                                        else:  # hour > 21.50
                                            if pres <= 1012.80:
                                                return 'Rain'
                                            else:  # pres > 1012.80
                                                return 'Cloudy'
                                    else:  # temp > 27.85
                                        if hour <= 20.50:
                                            if temp <= 27.95:
                                                return 'Clear'
                                            else:  # temp > 27.95
                                                return 'Clear'
                                        else:  # hour > 20.50
                                            if dew_point <= 25.92:
                                                return 'Clear'
                                            else:  # dew_point > 25.92
                                                if dew_point <= 26.22:
                                                    return 'Rain'
                                                else:  # dew_point > 26.22
                                                    return 'Clear'
                    else:  # rhum > 93.50
                        if latitude <= 34.10:
                            if hour <= 17.50:
                                if pres <= 1013.10:
                                    return 'Clear'
                                else:  # pres > 1013.10
                                    if pres <= 1014.10:
                                        return 'Fog'
                                    else:  # pres > 1014.10
                                        return 'Clear'
                            else:  # hour > 17.50
                                if pres <= 1011.95:
                                    if dew_point <= 22.58:
                                        return 'Rain'
                                    else:  # dew_point > 22.58
                                        if rhum <= 97.00:
                                            return 'Cloudy'
                                        else:  # rhum > 97.00
                                            return 'Cloudy'
                                else:  # pres > 1011.95
                                    return 'Clear'
                        else:  # latitude > 34.10
                            if rhum <= 96.50:
                                if hour <= 21.50:
                                    if pres <= 1005.75:
                                        if temp <= 24.15:
                                            if pres <= 1002.20:
                                                return 'Clear'
                                            else:  # pres > 1002.20
                                                if rhum <= 94.50:
                                                    return 'Rain'
                                                else:  # rhum > 94.50
                                                    return 'Rain'
                                        else:  # temp > 24.15
                                            if pres <= 1002.15:
                                                if temp <= 24.35:
                                                    return 'Clear'
                                                else:  # temp > 24.35
                                                    return 'Rain'
                                            else:  # pres > 1002.15
                                                if dew_point <= 26.28:
                                                    return 'Clear'
                                                else:  # dew_point > 26.28
                                                    return 'Rain'
                                    else:  # pres > 1005.75
                                        if temp <= 24.25:
                                            if pres <= 1010.60:
                                                if month <= 8.50:
                                                    return 'Rain'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                            else:  # pres > 1010.60
                                                if pres <= 1012.55:
                                                    return 'Clear'
                                                else:  # pres > 1012.55
                                                    return 'Rain'
                                        else:  # temp > 24.25
                                            if hour <= 16.50:
                                                if pres <= 1006.90:
                                                    return 'Clear'
                                                else:  # pres > 1006.90
                                                    return 'Rain'
                                            else:  # hour > 16.50
                                                if pres <= 1012.05:
                                                    return 'Clear'
                                                else:  # pres > 1012.05
                                                    return 'Clear'
                                else:  # hour > 21.50
                                    if pres <= 1007.90:
                                        if temp <= 26.75:
                                            return 'Rain'
                                        else:  # temp > 26.75
                                            if pres <= 1006.05:
                                                return 'Rain'
                                            else:  # pres > 1006.05
                                                return 'Clear'
                                    else:  # pres > 1007.90
                                        if dew_point <= 22.77:
                                            if pres <= 1013.10:
                                                return 'Cloudy'
                                            else:  # pres > 1013.10
                                                return 'Clear'
                                        else:  # dew_point > 22.77
                                            if temp <= 25.55:
                                                if pres <= 1008.55:
                                                    return 'Clear'
                                                else:  # pres > 1008.55
                                                    return 'Rain'
                                            else:  # temp > 25.55
                                                if pres <= 1011.80:
                                                    return 'Cloudy'
                                                else:  # pres > 1011.80
                                                    return 'Clear'
                            else:  # rhum > 96.50
                                if pres <= 1009.80:
                                    if dew_point <= 23.48:
                                        if pres <= 1003.05:
                                            if dew_point <= 22.93:
                                                if temp <= 21.95:
                                                    return 'Clear'
                                                else:  # temp > 21.95
                                                    return 'Rain'
                                            else:  # dew_point > 22.93
                                                if hour <= 16.50:
                                                    return 'Rain'
                                                else:  # hour > 16.50
                                                    return 'Rain'
                                        else:  # pres > 1003.05
                                            if pres <= 1008.95:
                                                if hour <= 14.50:
                                                    return 'Rain'
                                                else:  # hour > 14.50
                                                    return 'Rain'
                                            else:  # pres > 1008.95
                                                if temp <= 21.95:
                                                    return 'Clear'
                                                else:  # temp > 21.95
                                                    return 'Rain'
                                    else:  # dew_point > 23.48
                                        if rhum <= 97.50:
                                            if pres <= 1004.60:
                                                if month <= 7.50:
                                                    return 'Clear'
                                                else:  # month > 7.50
                                                    return 'Rain'
                                            else:  # pres > 1004.60
                                                return 'Clear'
                                        else:  # rhum > 97.50
                                            if month <= 6.50:
                                                if dew_point <= 23.82:
                                                    return 'Rain'
                                                else:  # dew_point > 23.82
                                                    return 'Clear'
                                            else:  # month > 6.50
                                                if rhum <= 99.50:
                                                    return 'Rain'
                                                else:  # rhum > 99.50
                                                    return 'Rain'
                                else:  # pres > 1009.80
                                    if temp <= 22.65:
                                        if hour <= 19.50:
                                            if hour <= 14.50:
                                                if pres <= 1012.80:
                                                    return 'Rain'
                                                else:  # pres > 1012.80
                                                    return 'Clear'
                                            else:  # hour > 14.50
                                                if month <= 8.50:
                                                    return 'Clear'
                                                else:  # month > 8.50
                                                    return 'Clear'
                                        else:  # hour > 19.50
                                            if month <= 8.00:
                                                if hour <= 22.00:
                                                    return 'Clear'
                                                else:  # hour > 22.00
                                                    return 'Cloudy'
                                            else:  # month > 8.00
                                                if dew_point <= 22.23:
                                                    return 'Cloudy'
                                                else:  # dew_point > 22.23
                                                    return 'Rain'
                                    else:  # temp > 22.65
                                        if month <= 8.50:
                                            if pres <= 1010.45:
                                                return 'Clear'
                                            else:  # pres > 1010.45
                                                if hour <= 20.50:
                                                    return 'Rain'
                                                else:  # hour > 20.50
                                                    return 'Rain'
                                        else:  # month > 8.50
                                            if temp <= 22.95:
                                                if rhum <= 98.50:
                                                    return 'Rain'
                                                else:  # rhum > 98.50
                                                    return 'Clear'
                                            else:  # temp > 22.95
                                                if rhum <= 99.50:
                                                    return 'Rain'
                                                else:  # rhum > 99.50
                                                    return 'Rain'