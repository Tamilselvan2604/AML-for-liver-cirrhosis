def findDecision(obj): #obj[0]: N_Days, obj[1]: Status, obj[2]: Drug, obj[3]: Age, obj[4]: Sex, obj[5]: Ascites, obj[6]: Hepatomegaly, obj[7]: Spiders, obj[8]: Edema, obj[9]: Bilirubin, obj[10]: Cholesterol, obj[11]: Albumin, obj[12]: Copper, obj[13]: Alk_Phos, obj[14]: SGOT, obj[15]: Tryglicerides, obj[16]: Platelets, obj[17]: Prothrombin
	# {"feature": "N_Days", "instances": 50, "metric_value": 0.1585, "depth": 1}
	if obj[0]>708.3372818581809:
		# {"feature": "Platelets", "instances": 44, "metric_value": 0.0946, "depth": 2}
		if obj[16]<=273.27328568181815:
			# {"feature": "Albumin", "instances": 23, "metric_value": 0.0637, "depth": 3}
			if obj[11]<=3.48:
				# {"feature": "Alk_Phos", "instances": 14, "metric_value": 0.1284, "depth": 4}
				if obj[13]>1828.0:
					# {"feature": "Prothrombin", "instances": 9, "metric_value": 0.1723, "depth": 5}
					if obj[17]>10.6:
						# {"feature": "Status", "instances": 5, "metric_value": 0.4899, "depth": 6}
						if obj[1] == 'C':
							return 1
						elif obj[1] == 'D':
							return 2
						elif obj[1] == 'CL':
							return 2
						else: return 2.0
					elif obj[17]<=10.6:
						return 2.5
					else: return 2.5
				elif obj[13]<=1828.0:
					# {"feature": "Age", "instances": 5, "metric_value": 0.4, "depth": 5}
					if obj[3]<=22280:
						return 3
					elif obj[3]>22280:
						return 2
					else: return 2.0
				else: return 2.8
			elif obj[11]>3.48:
				# {"feature": "Copper", "instances": 9, "metric_value": 0.252, "depth": 4}
				if obj[12]>51.0:
					# {"feature": "Drug", "instances": 5, "metric_value": 0.4, "depth": 5}
					if obj[2] == 'Placebo':
						return 1
					elif obj[2] == 'D-penicillamine':
						return 2
					else: return 2.0
				elif obj[12]<=51.0:
					return 2.25
				else: return 2.25
			else: return 1.6666666666666667
		elif obj[16]>273.27328568181815:
			# {"feature": "Copper", "instances": 21, "metric_value": 0.0651, "depth": 3}
			if obj[12]<=159.0:
				# {"feature": "Alk_Phos", "instances": 19, "metric_value": 0.0853, "depth": 4}
				if obj[13]>466.0:
					# {"feature": "Tryglicerides", "instances": 17, "metric_value": 0.0914, "depth": 5}
					if obj[15]>90.0:
						# {"feature": "Cholesterol", "instances": 12, "metric_value": 0.1381, "depth": 6}
						if obj[10]>232.0:
							# {"feature": "Age", "instances": 10, "metric_value": 0.1551, "depth": 7}
							if obj[3]<=15730:
								# {"feature": "Spiders", "instances": 5, "metric_value": 0.4899, "depth": 8}
								if obj[7] == 'N':
									return 1
								elif obj[7] == 'Y':
									return 2
								else: return 2.0
							elif obj[3]>15730:
								return 1
							else: return 1.0
						elif obj[10]<=232.0:
							return 2
						else: return 2.0
					elif obj[15]<=90.0:
						return 1
					else: return 1.0
				elif obj[13]<=466.0:
					return 2
				else: return 2.0
			elif obj[12]>159.0:
				return 2
			else: return 2.0
		else: return 1.380952380952381
	elif obj[0]<=708.3372818581809:
		return 3
	else: return 3.0
