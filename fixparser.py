import sys

# Mapping of FIX tag numbers to their corresponding tag names
tag_mapping = {
    '8': 'BeginString',
    '9': 'BodyLength',
    '35': 'MsgType',
    '49': 'SenderCompID',
    '56': 'TargetCompID',
    '34': 'MsgSeqNum',
    '52': 'SendingTime',
    '10': 'CheckSum',
    '11': 'ClOrdID',
    '37': 'OrderID',
    '41': 'OrigClOrdID',
    '54': 'Side',
    '38': 'OrderQty',
    '40': 'OrdType',
    '44': 'Price',
    '59': 'TimeInForce',
    '150': 'ExecType',
    '39': 'OrdStatus',
    '55': 'Symbol',
    '48': 'SecurityID',
    '22': 'SecurityIDSource',
    '58': 'Text',
    '60': 'TransactTime',
    '571': 'TradeReportID',
    '1003': 'TradeID',
    '487': 'TradeReportTransType',
    '856': 'TradeReportType',
    '828': 'TrdType',
    '1123': 'TradeHandlingInstr',
    '939': 'TrdRptStatus',
    '751': 'TradeReportRejectReason',
    '818': 'SecondaryTradeReportID',
    '32': 'LastQty',
    '31': 'LastPx',
    '64': 'SettlDate',
    '552': 'NoSides',
    
    '453': 'NoPartyIDs',
    '448': 'PartyID',
    '447': 'PartyIDSource',
    '452': 'PartyRole',
    '2376': 'PartyRoleQualifier',
    '1': 'Account',
    '581': 'AccountType',
    '528': 'OrderCapacity',
    '529': 'OrderRestrictions',
    '1724': 'OrderOrigination',
    '20011': 'FeeStructureID',
    '117': 'QuoteID',
    '297': 'QuoteStatus',
    '300': 'QuoteRejectReason',
    '296': 'NoQuoteSets',
    '302': 'QuoteSetID',
    '304': 'TotNoQuoteEntries',
    '299': 'QuoteEntryID',
    '132': 'BidPx',
    '133': 'OfferPx',
    '134': 'BidSize',
    '135': 'OfferSize',
    '2362': 'SelfMatchPreventionID',
    '20003': 'MarketMakerCommandID',
    '20009': 'MarketMakerCommandAction',
    '20004': 'MarketMakerCommandResult',
    '20005': 'MarketMakerCommandRejectionCode',
    '1369': 'MassActionReportID',
    '530': 'MassCancelRequestType',
    '531': 'MassCancelResponse',
    '532': 'MassCancelRejectReason',
}

# Mapping of MsgType values to their corresponding message names
msg_type_mapping = {
    '0': 'Heartbeat',
    '1': 'TestRequest',
    '2': 'ResendRequest',
    '3': 'Reject',
    '4': 'SequenceReset',
    '5': 'Logout',
    '6': 'ExecutionReport',
    '7': 'OrderCancelReject',
    'A': 'Logon',
    'D': 'NewOrderSingle',
    'F': 'OrderCancelRequest',
    'G': 'OrderCancelReplaceRequest',
    'J': 'BusinessMessageReject',
    'AE': 'TradeCaptureReport',
    'AR': 'TradeCaptureReportAck',
    'i': 'MassQuote',
    'b': 'MassQuoteAck',
    'UE': 'RequestForExecution',
    'UB': 'MarketMakerCommand',
    'UC': 'MarketMakerCommandAck',
    'r': 'OrderMassCancelReport',
    'q': 'OrderMassCancelRequest',
    'UU': 'BidOfferUpdate',
}

def parse_fix_message(line, line_number):
    fields = line.strip().split('|')
    parsed_message = []
    msg_type_value = None
    for field in fields:
        if '=' in field:
            tag, value = field.split('=', 1)
            tag_name = tag_mapping.get(tag, f'UnknownTag_{tag}')
            if tag == '35':  # MsgType
                msg_type_value = value
                tag_name = 'MsgType'
                value = f"{value} ({msg_type_mapping.get(value, 'UnknownMsgType')})"
            parsed_message.append(f"{tag_name}: {value}")
    return parsed_message

def main(input_file):
    with open(input_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            parsed_message = parse_fix_message(line, line_number)
            print(f"Line {line_number}")
            for field in parsed_message:
                print(field)
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_fix.py <input_file>")
    else:
        main(sys.argv[1])