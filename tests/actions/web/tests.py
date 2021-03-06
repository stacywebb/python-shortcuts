from shortcuts import Shortcut
from shortcuts.actions import URLAction, GetURLAction


class TestURLAction:
    def test_get_parameters(self):
        url = 'https://aleks.sh'
        action = URLAction(data={'url': url})

        dump = action._get_parameters()

        exp_dump = {
            'WFURLActionURL': url,
        }
        assert dump == exp_dump


class TestGetURLAction:
    toml_string = '''
        [[action]]
        type = "get_url"
        method = "POST"
        advanced = true

            [[action.headers]]
            key = "header1"
            value = "value"

            [[action.headers]]
            key = "authorization"
            value = "{{authorization}}"

            [[action.json]]
            key = "k"
            value = "v"
    '''

    def test_loads_from_toml(self):
        sc = Shortcut.loads(self.toml_string)

        assert len(sc.actions) == 1

        action = sc.actions[0]
        assert isinstance(action, GetURLAction) is True

        exp_data = {
            'headers': [
                {'key': 'header1', 'value': 'value'},
                {'key': 'authorization', 'value': '{{authorization}}'},
            ],
            'json': [
                {'key': 'k', 'value': 'v'},
            ],
            'advanced': True,
            'method': 'POST',
        }
        assert action.data == exp_data

    def test_dumps_to_plist(self):
        sc = Shortcut.loads(self.toml_string)
        dump = sc.dumps(file_format='plist')

        exp_dump = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n\t<key>WFWorkflowActions</key>\n\t<array>\n\t\t<dict>\n\t\t\t<key>WFWorkflowActionIdentifier</key>\n\t\t\t<string>is.workflow.actions.downloadurl</string>\n\t\t\t<key>WFWorkflowActionParameters</key>\n\t\t\t<dict>\n\t\t\t\t<key>Advanced</key>\n\t\t\t\t<true/>\n\t\t\t\t<key>ShowHeaders</key>\n\t\t\t\t<true/>\n\t\t\t\t<key>WFHTTPBodyType</key>\n\t\t\t\t<string>Json</string>\n\t\t\t\t<key>WFHTTPHeaders</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>WFDictionaryFieldValueItems</key>\n\t\t\t\t\t\t<array>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>header1</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>value</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>authorization</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t<key>{0, 1}</key>\n\t\t\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>Type</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>Variable</string>\n\t\t\t\t\t\t\t\t\t\t\t\t<key>VariableName</key>\n\t\t\t\t\t\t\t\t\t\t\t\t<string>authorization</string>\n\t\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>￼</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</array>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFDictionaryFieldValue</string>\n\t\t\t\t</dict>\n\t\t\t\t<key>WFHTTPMethod</key>\n\t\t\t\t<string>POST</string>\n\t\t\t\t<key>WFJSONValues</key>\n\t\t\t\t<dict>\n\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t<dict>\n\t\t\t\t\t\t<key>WFDictionaryFieldValueItems</key>\n\t\t\t\t\t\t<array>\n\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t<key>WFItemType</key>\n\t\t\t\t\t\t\t\t<integer>0</integer>\n\t\t\t\t\t\t\t\t<key>WFKey</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>k</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t<key>WFValue</key>\n\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t<key>Value</key>\n\t\t\t\t\t\t\t\t\t<dict>\n\t\t\t\t\t\t\t\t\t\t<key>attachmentsByRange</key>\n\t\t\t\t\t\t\t\t\t\t<dict/>\n\t\t\t\t\t\t\t\t\t\t<key>string</key>\n\t\t\t\t\t\t\t\t\t\t<string>v</string>\n\t\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t\t\t\t\t<string>WFTextTokenString</string>\n\t\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t\t</dict>\n\t\t\t\t\t\t</array>\n\t\t\t\t\t</dict>\n\t\t\t\t\t<key>WFSerializationType</key>\n\t\t\t\t\t<string>WFDictionaryFieldValue</string>\n\t\t\t\t</dict>\n\t\t\t</dict>\n\t\t</dict>\n\t</array>\n\t<key>WFWorkflowClientRelease</key>\n\t<string>2.0</string>\n\t<key>WFWorkflowClientVersion</key>\n\t<string>700</string>\n\t<key>WFWorkflowIcon</key>\n\t<dict>\n\t\t<key>WFWorkflowIconGlyphNumber</key>\n\t\t<integer>59511</integer>\n\t\t<key>WFWorkflowIconImageData</key>\n\t\t<data>\n\t\t</data>\n\t\t<key>WFWorkflowIconStartColor</key>\n\t\t<integer>431817727</integer>\n\t</dict>\n\t<key>WFWorkflowImportQuestions</key>\n\t<array/>\n\t<key>WFWorkflowInputContentItemClasses</key>\n\t<array>\n\t\t<string>WFAppStoreAppContentItem</string>\n\t\t<string>WFArticleContentItem</string>\n\t\t<string>WFContactContentItem</string>\n\t\t<string>WFDateContentItem</string>\n\t\t<string>WFEmailAddressContentItem</string>\n\t\t<string>WFGenericFileContentItem</string>\n\t\t<string>WFImageContentItem</string>\n\t\t<string>WFiTunesProductContentItem</string>\n\t\t<string>WFLocationContentItem</string>\n\t\t<string>WFDCMapsLinkContentItem</string>\n\t\t<string>WFAVAssetContentItem</string>\n\t\t<string>WFPDFContentItem</string>\n\t\t<string>WFPhoneNumberContentItem</string>\n\t\t<string>WFRichTextContentItem</string>\n\t\t<string>WFSafariWebPageContentItem</string>\n\t\t<string>WFStringContentItem</string>\n\t\t<string>WFURLContentItem</string>\n\t</array>\n\t<key>WFWorkflowTypes</key>\n\t<array>\n\t\t<string>NCWidget</string>\n\t\t<string>WatchKit</string>\n\t</array>\n</dict>\n</plist>\n'

        assert dump == exp_dump
